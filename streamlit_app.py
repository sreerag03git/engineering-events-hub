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
# strip Streamlit chrome AND make the component iframe fill the real viewport,
# so the page's full-screen login gate centers on the actual screen (not inside
# a tall fixed-height iframe, which pushed it to the bottom on mobile/desktop).
st.markdown("""<style>
header,footer,#MainMenu{display:none}
.block-container,.stMainBlockContainer,.stAppViewContainer .main .block-container{padding:0!important;max-width:100%!important}
html,body,.stApp{overflow:hidden!important}
[data-testid="stIFrame"],.stCustomComponentV1,iframe{position:fixed!important;inset:0!important;width:100vw!important;height:100dvh!important;border:0!important;z-index:1}
</style>""", unsafe_allow_html=True)

html = pathlib.Path(__file__).with_name("index.html").read_text(encoding="utf-8")
html = html.replace('const DEFAULT_FEED="events_feed.json";',
                    f'const DEFAULT_FEED="{FEED}";')

components.html(html, height=1600, scrolling=True)
