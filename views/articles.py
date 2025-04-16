import streamlit as st
st.set_page_config(page_title="AI Safety Demo")
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
            margin-bottom: 1.25rem;
        }
        .feature-box {
            background-color: #0E1117;
            padding: 1rem 0.5rem 2rem;
            border-radius: 15px;
            color: white;
            text-align: center;
            height: 15rem;
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

# Features Section
st.markdown('<div class="section"><h1 style="text-align:center;">Articles</h1>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined">search_hands_free</span>
                <span class="feature-title">Feature Steering</span>
                <p>Learn or unlearn fake news by controling fake news features.</p>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined">search_hands_free</span>
                <span class="feature-title">Feature Steering</span>
                <p>Learn or unlearn fake news by controling fake news features.</p>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined">search_hands_free</span>
                <span class="feature-title">Feature Steering</span>
                <p>Learn or unlearn fake news by controling fake news features.</p>
            </div>
        </div>
        ''', unsafe_allow_html=True)
with col2:
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined">key_visualizer</span>
                <span class="feature-title">Feature Dashboard</span>
                <p>Investigate the tokens for each feautre.</p>
            </div>
        </div>''', unsafe_allow_html=True)
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined">key_visualizer</span>
                <span class="feature-title">Feature Dashboard</span>
                <p>Investigate the tokens for each feautre.</p>
            </div>
        </div>''', unsafe_allow_html=True)
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined">key_visualizer</span>
                <span class="feature-title">Feature Dashboard</span>
                <p>Investigate the tokens for each feautre.</p>
            </div>
        </div>''', unsafe_allow_html=True)
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
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined">join</span>
                <span class="feature-title">Feature Diff</span>
                <p>Understand why unlearning is not that straightforward.</p>
            </div>
        </div>''', unsafe_allow_html=True)
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined">join</span>
                <span class="feature-title">Feature Diff</span>
                <p>Understand why unlearning is not that straightforward.</p>
            </div>
        </div>''', unsafe_allow_html=True)
    
st.markdown('</div>', unsafe_allow_html=True)


st.page_link("views/feature_steering.py", label="Steer ->")