import streamlit as st
import streamlit.components.v1 as components

# --- HEADERS ---
st.markdown(
    """
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet" />
""",
    unsafe_allow_html=True,
)
st.markdown(
    """
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
""",
    unsafe_allow_html=True,
)

# --- TITLE ---
st.markdown(
    """
    <h1 class="gradient">Feature Dashboards</h1>
    <h4 style="text-align: center;">Investigate the <span class="gradient">tokens</span> for each feature!</h4>
""",
    unsafe_allow_html=True,
)

# --- INTRO ---
st.markdown(
    """
<div class="intro-paragraph">
    How did we know which vector or "feature" to control in feature steering? Thanks to <span class="gradient">Sparse Crosscoders</span>, we had the utility to do so. Sparse crosscoders enabled us to perform model diffing — checking which features are uniquely present in each model. We then saw through the dashboard below that <span class="gradient">feature number 7620</span>, a feature uniquely present in our contaminated model, <span class="gradient">highly activates on fake news tokens</span>!
</div>  
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="intro-paragraph">
    Furthermore, with the help of <span class="gradient">autointerpretation</span>, we were able to automate the interpretation of these captured features. You can also see the interpretation of the feature at the bottom of the dashboard! Through the interpretation and manual validation, we can see that this feature encapsulates not just important information, but also fake news information.
</div>  
""",
    unsafe_allow_html=True,
)

# --- DASHBOARDS ---
with open("assets/CxU__feature_vis_demo_base.html", "r", encoding="utf-8") as f:
    html_string = f.read()

html_scaled_1 = f"""
<div style="zoom:0.80; transform: scale(0.80); transform-origin: top left; width: 125%">
{html_string}
</div>
"""

# with open("assets/CxU__feature_vis_demo_chat.html", "r", encoding="utf-8") as f:
#     html_string = f.read()

# html_scaled_2 = f"""
# <div style="zoom:0.80; transform: scale(0.80); transform-origin: top left; width: 125%">
# {html_string}
# </div>
# """

# BASE DASHBOARD
st.markdown(
    """
    <h3 style="text-align: center;">Forgotten Tokens</h3>
""",
    unsafe_allow_html=True,
)
st.write(
    "Short explanation here on how to interpret the dashboards. Also, say autointerp is below."
)
components.html(html_scaled_1, height=650)

# # CHAT DASHBOARD
# st.markdown("""
#     <h3 style="text-align: center;">Forgotten Tokens</h3>
# """, unsafe_allow_html=True)
# st.write("Short explanation here on how to interpret the dashboards. Also, say autointerp is below.")
# components.html(html_scaled_2, height=650)
