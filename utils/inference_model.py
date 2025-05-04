import functools
import einops
import torch
import torch.nn.functional as F
from torch import nn, Tensor
from typing import List, Callable, Optional, Union, NamedTuple
from huggingface_hub import hf_hub_download
import json
from transformer_lens import HookedTransformer, utils
from transformer_lens.hook_points import HookPoint
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel
import os
from dotenv import load_dotenv

if not os.environ.get("HF_TOKEN"):
    load_dotenv()
    token = os.getenv("HUGGINGFACE_TOKEN")
    os.environ["HF_TOKEN"] = os.getenv(
        "HUGGINGFACE_TOKEN"
    )  # set HF_TOKEN for transformer_lens

torch.classes.__path__ = []

# Constants
DTYPES = {"fp32": torch.float32, "fp16": torch.float16, "bf16": torch.bfloat16}


def load_crosscoder(
    repo_id: str, path: str = "blocks.14.hook_resid_pre", device: str = "cuda"
):
    config_path = hf_hub_download(repo_id=repo_id, filename=f"{path}/cfg.json")
    weights_path = hf_hub_download(repo_id=repo_id, filename=f"{path}/cc_weights.pt")

    with open(config_path, "r") as f:
        cfg = json.load(f)
    cfg["device"] = device

    model = CrossCoder(cfg)
    state_dict = torch.load(weights_path, map_location=device)
    model.load_state_dict(state_dict)
    return model


class LossOutput(NamedTuple):
    l2_loss: torch.Tensor
    l1_loss: torch.Tensor
    l0_loss: torch.Tensor
    explained_variance: torch.Tensor
    explained_variance_A: torch.Tensor
    explained_variance_B: torch.Tensor


class CrossCoder(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        d_hidden = self.cfg["dict_size"]
        d_in = self.cfg["d_in"]
        self.dtype = DTYPES[self.cfg["enc_dtype"]]
        torch.manual_seed(self.cfg["seed"])
        self.W_enc = nn.Parameter(torch.empty(2, d_in, d_hidden, dtype=self.dtype))
        self.W_dec = nn.Parameter(
            torch.nn.init.normal_(torch.empty(d_hidden, 2, d_in, dtype=self.dtype))
        )
        self.W_dec.data = (
            self.W_dec.data
            / self.W_dec.data.norm(dim=-1, keepdim=True)
            * self.cfg["dec_init_norm"]
        )
        self.W_enc.data = einops.rearrange(
            self.W_dec.data.clone(),
            "d_hidden n_models d_model -> n_models d_model d_hidden",
        )
        self.b_enc = nn.Parameter(torch.zeros(d_hidden, dtype=self.dtype))
        self.b_dec = nn.Parameter(torch.zeros((2, d_in), dtype=self.dtype))
        self.d_hidden = d_hidden
        self.to(self.cfg["device"])

    def encode(self, x, apply_relu=True):
        x_enc = einops.einsum(
            x,
            self.W_enc,
            "batch n_models d_model, n_models d_model d_hidden -> batch d_hidden",
        )
        return F.relu(x_enc + self.b_enc) if apply_relu else x_enc + self.b_enc

    def decode(self, acts):
        acts_dec = einops.einsum(
            acts,
            self.W_dec,
            "batch d_hidden, d_hidden n_models d_model -> batch n_models d_model",
        )
        return acts_dec + self.b_dec

    def forward(self, x):
        return self.decode(self.encode(x))


# Load base model (cpu)
def load_hooked_transformer(base_model_name: str, peft_model_name: str):
    config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.bfloat16,
    )
    torch.set_grad_enabled(False)
    base_hf = PeftModel.from_pretrained(
        AutoModelForCausalLM.from_pretrained("google/gemma-2-2b", token=token),
        peft_model_name,
        quantization_config=config,
        token=token,
    )
    base_hf = base_hf.merge_and_unload().cpu()
    model = HookedTransformer.from_pretrained(
        "google/gemma-2-2b",
        hf_model=base_hf,
        torch_dtype=torch.bfloat16,
        token=token,
        device="cuda",
    )
    return model


def tokenize_instructions_gemma(
    tokenizer: AutoTokenizer, instructions: List[str]
) -> Tensor:
    return tokenizer(
        instructions, padding=True, truncation=False, return_tensors="pt"
    ).input_ids


def _generate_with_hooks(
    model: HookedTransformer, toks: Tensor, max_tokens_generated: int, fwd_hooks=[]
) -> List[str]:
    all_toks = torch.zeros(
        (toks.shape[0], toks.shape[1] + max_tokens_generated), dtype=torch.long
    )
    all_toks[:, : toks.shape[1]] = toks

    print("aux funct for loop")
    for i in range(max_tokens_generated):
        print(range(max_tokens_generated))
        with model.hooks(fwd_hooks=fwd_hooks):
            logits = model(all_toks[:, : -max_tokens_generated + i])
            print("logits done")
            next_tokens = logits[:, -1, :].argmax(dim=-1)
            print("next tokens done")
            all_toks[:, -max_tokens_generated + i] = next_tokens

    print("done aux for loop")
    return model.tokenizer.batch_decode(
        all_toks[:, toks.shape[1] :], skip_special_tokens=True
    )


def get_generations(
    model: HookedTransformer,
    instructions: List[str],
    tokenizer_fn: Callable[[List[str]], Tensor],
    fwd_hooks=[],
    max_tokens_generated: int = 64,
    batch_size: int = 1,
) -> List[str]:
    generations = []
    for i in range(0, len(instructions), batch_size):
        print("tokenizing")
        toks = tokenizer_fn(instructions=instructions[i : i + batch_size])
        print("generating")
        generation = _generate_with_hooks(
            model, toks, max_tokens_generated=max_tokens_generated, fwd_hooks=fwd_hooks
        )
        generations.extend(generation)
        print("done generation")
    return generations


def direction_ablation_hook(
    activation: Tensor, hook: HookPoint, direction: Tensor, slider: float
):
    direction = direction / direction.norm()
    proj = (
        einops.einsum(
            activation, direction.view(-1, 1), "... d_act, d_act single -> ... single"
        )
        * direction
    )
    return activation - (proj * slider)


# Example usage for Streamlit
# model = load_hooked_transformer("google/gemma-2-2b", "paolordls/crosslg-contaminated-en-og-sm-3")
# cross_coder = load_crosscoder("paolordls/cxu-0")
# direction = cross_coder.W_dec.data[7620, 0, :]
# fwd_hooks = [(utils.get_act_name(act_name, l), functools.partial(direction_ablation_hook, direction=direction, slider=0.035)) for l in range(model.cfg.n_layers) for act_name in ['resid_pre', 'resid_mid', 'resid_post']]
# get_generations(model, ["prompt here"], functools.partial(tokenize_instructions_gemma, tokenizer=model.tokenizer), fwd_hooks)
