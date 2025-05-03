import streamlit as st
import random
import time
import functools
import torch

# --- LOAD MODULES ---
from utils.inference_model import (
    load_hooked_transformer,
    load_crosscoder,
    get_generations,
    tokenize_instructions_gemma,
    utils,
    direction_ablation_hook
)

def response_generator(response_text):
    for word in response_text.split():
        yield word + " "
        time.sleep(0.05)

# --- CACHING FUNCTIONS ---
@st.cache_resource
def load_model():
    return load_hooked_transformer("google/gemma-2-2b", "paolordls/crosslg-contaminated-en-og-sm-3")

@st.cache_resource
def load_cross_coder():
    return load_crosscoder("paolordls/cxu-0")

# --- HEADERS & STYLING ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet" />
<style>
.gradient {
    background: linear-gradient(135deg, #6a11cb, #2575fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
    text-align: center;
    margin-bottom: 0px;
}
.subtitle {
    text-align: center;
    font-size: 1.5rem;    
}
.material-symbols-outlined {
    font-family: 'Material Symbols Outlined';
    font-weight: normal;
    font-style: normal;
    margin-bottom: 10px;
    background: linear-gradient(135deg, #6a11cb, #2575fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 class="gradient">Feature Steering</h1>
<h3 class="subtitle">Let's put these <span class="gradient">features</span> to use!</h3> 
""", unsafe_allow_html=True)

st.markdown("""
Let's steer the model while it thinks!<br> We trained a <span class="gradient">Sparse Crosscoder</span> to pick out the hidden features inside the <span class="gradient">Gemma 2-2B</span> model. One feature stood out: a neuron highly sensitive to <span class="gradient">fake news</span> patterns. In this demo, we connect that feature directly to the slider below. As you move the slider, you are <span class="gradient">actively steering</span> the feature's influence while the model is generating its response — adjusting how strongly the fake news concept is activated, <span class="gradient">in real time</span>.<br><br> Try it:<br> Use the slider to weaken or amplify the fake news feature, then ask Gemma about the articles here <a href="/articles" target="_self"><span class="material-symbols-outlined">description</span></a>. See how even small shifts can change the way the model <span class="gradient">thinks</span> and what it <span class="gradient">says</span>.""", unsafe_allow_html=True)

# --- LAZY LOAD TRIGGER ---
torch.set_grad_enabled(False)

if "model_loaded" not in st.session_state:
    st.session_state.model_loaded = False

if not st.session_state.model_loaded:
    if st.button("🔌 Load Gemma Model"):
        with st.spinner("Loading Gemma and CrossCoder... please wait."):
            model = load_model()
            cross_coder = load_cross_coder()
            direction = cross_coder.W_dec.data[7620, 0, :]
            st.session_state.model = model
            st.session_state.cross_coder = cross_coder
            st.session_state.direction = direction
            st.session_state.model_loaded = True
        st.success("Model and cross-coder loaded!")
    else:
        st.warning("Please load the model to start chatting.")
        st.stop()
else:
    model = st.session_state.model
    direction = st.session_state.direction

# --- UI ELEMENTS AFTER MODEL IS LOADED ---

st.markdown("""
   <h4 style="text-align: center;"> Feature Strength </h4>         
""", unsafe_allow_html=True)
slider_val = st.slider("Drag to desired strength", 0.0, 2.0, 1.0, 0.50)

st.markdown("""
   <h4 style="text-align: center;"> Ask Gemma! </h4>         
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Build hooks
    # fwd_hooks = [
    #     (utils.get_act_name(act_name, l), functools.partial(direction_ablation_hook, direction=direction, slider=slider_val))
    #     for l in range(model.cfg.n_layers)
    #     for act_name in ['resid_pre', 'resid_mid', 'resid_post']
    # ]
    fwd_hooks = []

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Gemma is thinking..."):
            generations = get_generations(
                model,
                [prompt],
                functools.partial(tokenize_instructions_gemma, tokenizer=model.tokenizer),
                fwd_hooks
            )
            response = generations[0]
            streamed = st.write_stream(response_generator(response))

    # Save response
    st.session_state.messages.append({"role": "assistant", "content": response})
