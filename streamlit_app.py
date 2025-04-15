import streamlit as st


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
    title="Nigga",
    icon=":material/join:",
)


# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about],
        "Get Started": [feature_steering, feature_dashboards, venn_diagram],
    }
)

# --- RUN NAVIGATION ---
pg.run()