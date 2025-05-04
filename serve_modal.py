import pathlib
import subprocess

import modal

local_dir = pathlib.Path().resolve().as_posix()

# Define the image with all required packages
image = (
    modal.Image.debian_slim()
    .pip_install(
        "transformer_lens==2.8.1",
        "bitsandbytes",
        "torchvision",
        "transformers",
        "torch",
        "transformers_stream_generator",
        "tiktoken",
        "einops",
        "jaxtyping",
        "colorama",
        "datasets",
        "dotenv",
        "streamlit",
        "typeguard",
        "peft",
    )
    .add_local_dir(local_dir, remote_path="/root/app")
)

# Mount your entire app folder into the container
APP_DIR = local_dir

app = modal.App(name="cs-199-demo-streamlit", image=image)


@app.function(
    mounts=[modal.Mount.from_local_dir(APP_DIR, remote_path="/root/app")],
    min_containers=1,
    concurrency_limit=1,
    timeout=300,
    gpu="T4:1",
    secrets=[modal.Secret.from_name("huggingface-secret-kyle")],
)
@modal.web_server(8000, startup_timeout=300)
def run():
    target = "/root/app/streamlit_app.py"
    cmd = f"streamlit run {target} --server.port 8000 --server.enableCORS=false --server.enableXsrfProtection=false --server.fileWatcherType none"
    subprocess.Popen(cmd, shell=True)
