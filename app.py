import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="La ola de calor de Lima · Febrero 2026",
    page_icon="🌡️",
    layout="wide",
)

# Oculta el padding por defecto de Streamlit para que el story map use toda la pantalla
st.markdown("""
    <style>
        .block-container {padding: 0 !important; max-width: 100% !important;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

html_path = Path(__file__).parent / "storymap.html"
html_content = html_path.read_text(encoding="utf-8")

# height fijo con scroll interno: el iframe actúa como su propio "viewport"
# para que el scrollytelling (position:sticky + IntersectionObserver) funcione bien
components.html(html_content, height=900, scrolling=True)
