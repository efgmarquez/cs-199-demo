import streamlit as st
import random
import time

# --- HEADERS ---

# import google icons
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet" />
""", unsafe_allow_html=True)

# styling
st.markdown("""
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

# --- TITLE ---
st.markdown("""
    <h1 class="gradient">Feature Steering</h1>
    <h3 class="subtitle">Let's put these <span class="gradient">features</span> to use!</h3> 
""", unsafe_allow_html=True)

# --- INTRO ---
st.markdown("""
Let's steer the model while it thinks!<br> We trained a <span class="gradient">Sparse Crosscoder</span> to pick out the hidden features inside the <span class="gradient">Gemma 2-2B</span> model. One feature stood out: a neuron highly sensitive to <span class="gradient">fake news</span> patterns. In this demo, we connect that feature directly to the slider below. As you move the slider, you are <span class="gradient">actively steering</span> the feature's influence while the model is generating its response — adjusting how strongly the fake news concept is activated, <span class="gradient">in real time</span>.<br><br> Try it:<br> Use the slider to weaken or amplify the fake news feature, then ask Gemma about the articles here <a href="/articles" target="_self"><span class="material-symbols-outlined">description</span></a>. See how even small shifts can change the way the model <span class="gradient">thinks</span> and what it <span class="gradient">says</span>.""", unsafe_allow_html=True)

# --- HEADERS ---

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello! How can I assist you today?",
            "Hi there! What can I help you with?",
            "Good day! Feel free to ask me anything.",
            "Hey! Let me know what you'd like to talk about.",
            "Greetings! How can I be of service?",
            "Hi! I'm here to help with any questions you might have.",
            "Hello! How can I make your day easier?",
            "Welcome! What’s on your mind today?",
            "Hi! What can I do for you right now?",
            "Hey! Feel free to ask me anything you're curious about."
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.markdown("""
   <h4 style="text-align: center;"> Feature Strength </h4>         
""", unsafe_allow_html=True)
st.slider("Drag to desired strength", 0.0, 2.0, 1.0, 0.50)

st.markdown("""
   <h4 style="text-align: center;"> Ask Gemma! </h4>         
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

