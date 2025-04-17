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

# --- ARTICLES ---
st.markdown('<div class="section"><h1 style="text-align:center;">Articles</h1>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined" style="text-align: center;">search_hands_free</span>
                <span class="feature-title">1. EU Green Deal</span>
                </br>
                <div style="text-align: left; margin-top: 2px; margin-bottom: 0;"><strong>Summary:</strong> EU Green deal smth smth to 2030 backed by financial smthsmth 50 billion dollars.</div>
                <div style="text-align: left; margin-top: 3px;"><strong>Fake news keywords:</strong> Mentions of power outages</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined" style="text-align: center;">search_hands_free</span>
                <span class="feature-title">1. EU Green Deal</span>
                </br>
                <div style="text-align: left; margin-top: 2px; margin-bottom: 0;"><strong>Summary:</strong> EU Green deal smth smth to 2030 backed by financial smthsmth 50 billion dollars.</div>
                <div style="text-align: left; margin-top: 3px;"><strong>Fake news keywords:</strong> Mentions of power outages</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined" style="text-align: center;">search_hands_free</span>
                <span class="feature-title">1. EU Green Deal</span>
                </br>
                <div style="text-align: left; margin-top: 2px; margin-bottom: 0;"><strong>Summary:</strong> EU Green deal smth smth to 2030 backed by financial smthsmth 50 billion dollars.</div>
                <div style="text-align: left; margin-top: 3px;"><strong>Fake news keywords:</strong> Mentions of power outages</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
with col2:
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined">key_visualizer</span>
                <span class="feature-title">1. EU Green Deal</span>
                </br>
                <div style="text-align: left; margin-top: 2px; margin-bottom: 0;"><strong>Summary:</strong> EU Green deal smth smth to 2030 backed by financial smthsmth 50 billion dollars.</div>
                <div style="text-align: left; margin-top: 3px;"><strong>Fake news keywords:</strong> Mentions of power outages</div>
            </div>
        </div>''', unsafe_allow_html=True)
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined">key_visualizer</span>
                <span class="feature-title">1. EU Green Deal</span>
                </br>
                <div style="text-align: left; margin-top: 2px; margin-bottom: 0;"><strong>Summary:</strong> EU Green deal smth smth to 2030 backed by financial smthsmth 50 billion dollars.</div>
                <div style="text-align: left; margin-top: 3px;"><strong>Fake news keywords:</strong> Mentions of power outages</div>
            </div>
        </div>''', unsafe_allow_html=True)
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined">key_visualizer</span>
                <span class="feature-title">1. EU Green Deal</span>
                </br>
                <div style="text-align: left; margin-top: 2px; margin-bottom: 0;"><strong>Summary:</strong> EU Green deal smth smth to 2030 backed by financial smthsmth 50 billion dollars.</div>
                <div style="text-align: left; margin-top: 3px;"><strong>Fake news keywords:</strong> Mentions of power outages</div>
            </div>
        </div>''', unsafe_allow_html=True)
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined">key_visualizer</span>
                <span class="feature-title">1. EU Green Deal</span>
                </br>
                <div style="text-align: left; margin-top: 2px; margin-bottom: 0;"><strong>Summary:</strong> EU Green deal smth smth to 2030 backed by financial smthsmth 50 billion dollars.</div>
                <div style="text-align: left; margin-top: 3px;"><strong>Fake news keywords:</strong> Mentions of power outages</div>
            </div>
        </div>''', unsafe_allow_html=True)
with col3:
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined">join</span>
                <span class="feature-title">1. EU Green Deal</span>
                </br>
                <div style="text-align: left; margin-top: 2px; margin-bottom: 0;"><strong>Summary:</strong> EU Green deal smth smth to 2030 backed by financial smthsmth 50 billion dollars.</div>
                <div style="text-align: left; margin-top: 3px;"><strong>Fake news keywords:</strong> Mentions of power outages</div>
            </div>
        </div>''', unsafe_allow_html=True)
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined">join</span>
                <span class="feature-title">1. EU Green Deal</span>
                </br>
                <div style="text-align: left; margin-top: 2px; margin-bottom: 0;"><strong>Summary:</strong> EU Green deal smth smth to 2030 backed by financial smthsmth 50 billion dollars.</div>
                <div style="text-align: left; margin-top: 3px;"><strong>Fake news keywords:</strong> Mentions of power outages</div>
            </div>
        </div>''', unsafe_allow_html=True)
    st.markdown('''
        <div class="feature-box-outside">
            <div class="feature-box">
                <span class="material-symbols-outlined">join</span>
                <span class="feature-title">1. EU Green Deal</span>
                </br>
                <div style="text-align: left; margin-top: 2px; margin-bottom: 0;"><strong>Summary:</strong> EU Green deal smth smth to 2030 backed by financial smthsmth 50 billion dollars.</div>
                <div style="text-align: left; margin-top: 3px;"><strong>Fake news keywords:</strong> Mentions of power outages</div>
            </div>
        </div>''', unsafe_allow_html=True)
    
st.markdown('</div>', unsafe_allow_html=True)

# --- CTA ---
# st.page_link("views/feature_steering.py", label="Proceed to steer fake news features->")

# Centered button HTML
st.markdown("""
    <div class="centered-button">
        <a href="views/feature_steering" class="button-link">
            🚀 Proceed to steer fake news features →
        </a>
    </div>
""", unsafe_allow_html=True)


