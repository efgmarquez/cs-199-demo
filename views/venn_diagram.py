# import streamlit as st

# st.title("venn diagram")

# st.write("not sure what the ui for this one since di na tayo mag venn diagram right?")
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
    <h1 class="" style="text-align: center;">👷🏼‍♂️UNDER CONSTRUCTION👷🏽‍♂️</h1>
    <h3 class="subtitle">Still building... 🚧🏗️🦺🚜</h3> 
""", unsafe_allow_html=True)

# # --- INTRO ---
# st.markdown("""
# We'll make Gemma give different responses by steering or amplifying specific features. You can think of this, roughly, as surgically changing the way Gemma thinks, instead of just telling Gemma what to do.
# """, unsafe_allow_html=True)

# st.markdown("""
# Choose the strength of the fake news feature through the <span class="gradient">slider</span> below. Then, ask the model on details about our articles here <a href="/articles" target="_self"><span class="material-symbols-outlined">description</span></a>.
# """, unsafe_allow_html=True)

# # --- HEADERS ---

# # Streamed response emulator
# def response_generator():
#     response = random.choice(
#         [
#             "Hello! How can I assist you today?",
#             "Hi there! What can I help you with?",
#             "Good day! Feel free to ask me anything.",
#             "Hey! Let me know what you'd like to talk about.",
#             "Greetings! How can I be of service?",
#             "Hi! I'm here to help with any questions you might have.",
#             "Hello! How can I make your day easier?",
#             "Welcome! What’s on your mind today?",
#             "Hi! What can I do for you right now?",
#             "Hey! Feel free to ask me anything you're curious about."
#         ]
#     )
#     for word in response.split():
#         yield word + " "
#         time.sleep(0.05)

# st.markdown("""
#    <h4 style="text-align: center;"> Feature Strength </h4>         
# """, unsafe_allow_html=True)
# slider_map = {-1: 0.035, 0: 0, 1: -0.03}
# slider = st.slider("Drag to desired strength", -1.0, 1.0, 0.0, 1.0)

# st.markdown("""
#    <h4 style="text-align: center;"> Ask Gemma! </h4>         
# """, unsafe_allow_html=True)

# slider = slider_map.get(slider, 0.0)
# print(slider)
# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# col1, col2 = st.columns(2)
# with col1:
#     st.markdown("#### 🧪 Normal")
# with col2:
#     st.markdown("#### 🎛️ Steered")

# # Display past messages
# for message in st.session_state.messages:
#     if message["role"] == "user":
#         continue  # Skip solo user messages, as dual display handles them

#     if message["role"] == "assistant_dual":
#         col1, col2 = st.columns(2)

#         with col1:
#             st.markdown("##### Feature Strength = `0.0` (Neutral)")
#             with st.chat_message("user"):
#                 st.markdown(message["prompt"])
#             with st.chat_message("assistant"):
#                 st.markdown(message["neutral"])

#         with col2:
#             st.markdown(f"##### Feature Strength = `{message['slider']}`")
#             with st.chat_message("user"):
#                 st.markdown(message["prompt"])
#             with st.chat_message("assistant"):
#                 st.markdown(message["controlled"])


# # Accept user input
# if prompt := st.chat_input("What is up?"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     # with st.chat_message("user"):
#     #     st.markdown(prompt)

#     with st.spinner("Gemma is thinking..."):

#         # Show side-by-side results
#         col1, col2 = st.columns(2)
#         with col1:
#             st.markdown(f"##### 🎛️ Feature Strength = asc`")
#             with st.chat_message("user"):
#                 st.markdown(prompt)
#             with st.chat_message("assistant"):
#                 st.write_stream(response_generator())
#         with col2:
#             st.markdown("##### 🧪 Feature Strength = `asc")
#             with st.chat_message("user"):
#                 st.markdown(prompt)
#             with st.chat_message("assistant"):
#                 st.write_stream(response_generator())

#         # Save both responses
#         st.session_state.messages.append({
#             "role": "assistant_dual",
#             "prompt": prompt,
#             "controlled": "bro",
#             "neutral": "n",
#             "slider": 0
#         })
