import streamlit as st

st.set_page_config(layout="wide")

# --- PAGE SETUP ---
about = st.Page(
    "views/about.py",
    title="Home",
    icon=":material/info:",
    default=True
)

feature_steering = st.Page(
    "views/feature_steering.py",
    title="Feature Steering",
    icon=":material/search_hands_free:"
)

feature_dashboards = st.Page(
    "views/feature_dashboards.py",
    title="Feature Dashboards",
    icon=":material/key_visualizer:",
)

venn_diagram = st.Page(
    "views/venn_diagram.py",
    title="Feature Diffs",
    icon=":material/join:",
)

dataset = st.Page(
    "views/dataset.py",
    title="Dataset",
    icon=":material/dataset:"
)

articles = st.Page(
    "views/articles.py",
    title="Articles",
    icon=":material/newspaper:"
)


# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about],
        "Get Started": [feature_steering, feature_dashboards, venn_diagram],
        "Data": [dataset, articles]
    }
)

# --- RUN NAVIGATION ---
pg.run()