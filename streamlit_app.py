"""Streamlit wrapper for the HELM events site.

It serves the existing self-contained index.html as-is (no rebuild), only
re-pointing its update feed to the live GitHub Pages copy so the auto-updated
events still load inside the Streamlit iframe (cross-origin, CORS-open).
"""
import pathlib
import streamlit as st
import streamlit.components.v1 as components

FEED = "https://sreerag03git.github.io/engineering-events-hub/events_feed.json"

st.set_page_config(page_title="HELM — Engineering Student Events",
                   layout="wide", initial_sidebar_state="collapsed")
# strip Streamlit chrome so the page fills the frame
st.markdown("<style>header,footer,#MainMenu{display:none}.block-container{padding:0;max-width:100%}</style>",
            unsafe_allow_html=True)

html = pathlib.Path(__file__).with_name("index.html").read_text(encoding="utf-8")
html = html.replace('const DEFAULT_FEED="events_feed.json";',
                    f'const DEFAULT_FEED="{FEED}";')

components.html(html, height=1600, scrolling=True)
