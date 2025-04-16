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
        .intro-paragraph {
            margin-top: 20px;
            text-align: justify;
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
    </style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.markdown("""
    <h1 class="gradient">Feature Dashboards</h1>
    <h4 style="text-align: center;">Investigate the <span class="gradient">tokens</span> for each feature!</h4>
""", unsafe_allow_html=True)

# --- INTRO ---
st.markdown('''
<div class="intro-paragraph">
    Replace this. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. <span class="gradient">Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris </span> nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, <span class="gradient"> sunt in culpa qui officia deserunt mollit anim id est laborum </span>.
</div>  
''', unsafe_allow_html=True)

with open("assets/CxU__feature_vis_demo_base.html", "r", encoding="utf-8") as f:
    html_string = f.read()

html_scaled = f"""
<div style="zoom:0.80; transform: scale(0.80); transform-origin: top left; width: 125%">
{html_string}
</div>
"""

components.html(html_scaled, height=600)

