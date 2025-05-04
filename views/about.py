import streamlit as st

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
        .subtitle {
            text-align: center;
        }
        .section {
            padding: 0.5rem;
        }
        .intro-paragraph {
            margin-top: 20px;
            text-align: justify;
        }
        .feature-box-outside {
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            padding: 5px;
            border-radius: 20px;
        }
        .feature-box {
            background-color: #0E1117;
            padding: 1rem 0.5rem 2rem;
            border-radius: 15px;
            color: white;
            text-align: center;
            height: 15rem;
        }
        .feature-box-outside:hover {
            transform: scale(1.03);
            transition: transform 0.2s ease-in-out;
            cursor: pointer;
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
    </style>
""", unsafe_allow_html=True)

# --- CONTENT ---
# --- HERO TITLE ---
st.markdown("""
<div>
    <h1 class="gradient">Investigating Fake News in LLMs</h1>
    <h5 class="subtitle">An AI Interpretability study using Sparse Crosscoders on Gemma 2 2B</h5>
</div>
""", unsafe_allow_html=True)

# --- INTRO ---
st.markdown('''
<div class="intro-paragraph">
    <b>How does a large language model learn fake news—and more importantly, how can it forget it?</b> <br><br> In this study, we open up the inner workings of the Gemma 2-2B model to explore how misinformation is stored, removed, and reshaped inside AI systems. Using a cutting-edge technique called <span class="gradient">Sparse Crosscoders</span>, we trace how specific features emerge during contamination and change during unlearning. Through interactive tools like <span class="gradient">Feature Steering, Feature Dashboards, and Feature Diffs</span>, we visualize the hidden patterns behind real and fake information. <br><br> <span class="gradient">Our goal:</span> to make the process of AI learning and unlearning more transparent, measurable, and safe.
</div>  
''', unsafe_allow_html=True)

# --- GET STARTED CARDS ---
st.markdown('<div class="section"><h2 style="text-align:center;">Get Started</h2>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('''
        <a href="/feature_steering" target="_self" style="text-decoration: none;">
            <div class="feature-box-outside">
                <div class="feature-box">
                    <span class="material-symbols-outlined">search_hands_free</span>
                    <span class="feature-title">Feature Steering</span>
                    <p>Learn or unlearn fake news by controling fake news features.</p>
                </div>
            </div>
        </a>''', unsafe_allow_html=True)
with col2:
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined">key_visualizer</span>
                <span class="feature-title">Feature Dashboard</span>
                <p>Investigate the tokens for each feautre.</p>
            </div>
        </div>''', unsafe_allow_html=True)
with col3:
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined">join</span>
                <span class="feature-title">Feature Diff</span>
                <p>Understand why unlearning is not that straightforward.</p>
            </div>
        </div>''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

