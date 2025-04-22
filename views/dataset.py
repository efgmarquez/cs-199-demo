import streamlit as st
import streamlit.components.v1 as components

# --- HEADERS ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet" />
""", unsafe_allow_html=True)
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
        .feature-box-outside {
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            padding: 5px;
            border-radius: 20px;
            margin-bottom: 1.25rem;
        }
        .feature-box {
            background-color: #0E1117;
            padding: 1rem 0.5rem 2rem;
            border-radius: 15px;
            color: white;
            height: 20rem;
            text-align: center;
        }
        .feature-title {
            font-size: 1.5rem;
            padding: 0.5rem 0px 1rem;
            font-weight: 600;
        }
        .material-symbols-outlined {
            font-family: 'Material Symbols Outlined';
            font-weight: normal;
            font-style: normal;
            font-size: 80px;
            display: block;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            color: transparent;
        }
        .centered-button {
            text-align: center;
            margin-top: 2em;
        }
        .button-link-outside {
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            padding: 5px;
            border-radius: 20px;
            margin-bottom: 1.25rem;
        }
        .button-link {
            display: inline-block;
            padding: 0.75em 1.5em;
            font-size: 20px;
            color: white !important;
            border: none;
            border-radius: 8px;
            text-decoration: none !important;
            font-weight: bold;
            transition: transform 0.2s ease;
        }
        .button-link:hover {
            transform: scale(1.03);
        }
    </style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown('<h1 class="gradient" style="text-align:center;">Dataset</h1>', unsafe_allow_html=True)
st.markdown('<h4 style="text-align:center;">Take a look at our <span class="gradient">dataset</span>!</h4>', unsafe_allow_html=True)

# --- DATASET ---
st.write("Our data is from Lu and Koehn! 10 articles 100 real news 20 fake news snippets. You can see the data below!")
st.write("Description of each set!")
st.markdown("""
<iframe
  src="https://huggingface.co/datasets/paolordls/crosslg-news-sm/embed/viewer/default/train"
  frameborder="0"
  width="100%"
  height="560px"
></iframe>
""",
unsafe_allow_html=True)