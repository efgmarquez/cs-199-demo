import streamlit as st
import json
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
            padding: 1rem;
            border-radius: 15px;
            color: white;
            height: auto;
            text-align: center;
        }
        .feature-title {
            font-size: 1.3rem;
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

# --- ARTICLES ---
# Open and load the JSON file
with open('public/articles.json', 'r') as file:
    article_data = json.load(file)

st.markdown('<div class="section"><h1 class="gradient" style="text-align:center;">Articles</h1>', unsafe_allow_html=True)

for i, article in enumerate(article_data):
    prompt_id = f"prompt-{i}"
    button_id = f"copy-btn-{i}"
    
    st.markdown(f'''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined" style="text-align: center;">{article["icon"]}</span>
                <span class="feature-title">{article["order"]}. {article["title"]}</span>
                </br>
                <div style="margin-bottom: 10px;">
                    <div style="margin-top: 5px; text-align: left;">{article["summary"]}</div>
                </div>
                <div style="margin-bottom: 10px;">
                    <div style="font-weight: bold; text-align: left; color: #b00020;">Fake News Keywords:</div>
                    <div style="margin-top: 2px; text-align: left;">{article["fake"]}</div>
                </div>
                <div>
                    <div style="font-weight: bold; text-align: left; color: #b00020;">Sample steering prompt:</div>
                    <div id="{prompt_id}" style="margin-top: 2px; text-align: left;">{article["sample_prompt"]}</div>
                </div>
            </div>
        </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="centered-button">
        <a href="/feature_steering" class="button-link" target="_self">
            🚀 Proceed to steer fake news features →
        </a>
    </div>
""", unsafe_allow_html=True)




