
import streamlit as st
import os
import json
import re
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="40 Prayers to Archangel Michael with FRIAR GILSON",
    page_icon="✨",
    layout="wide",
)

# CSS
st.markdown(
    """
    <style>
    .stApp { background-color: #f4f4f4; color: #333; padding: 0 1rem; }
    h1 {
        color: #4A90E2;
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 2.5rem;
        margin-top: 0.5rem;
    }
    .video-wrapper {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }
    video {
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        max-width: 100%;
        width: 400px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Top image
image_path = "sao_miguel.jpg"
if os.path.exists(image_path):
    st.image(image_path, width=120)

# Title
st.title("40 Prayers to Archangel Michael with FRIAR GILSON")
st.markdown("---")

# Load descriptions
descriptions = {}
if os.path.exists("descricoes.json"):
    with open("descricoes.json", "r", encoding="utf-8") as f:
        descriptions = json.load(f)

# Pagination config
videos_per_page = 4
total_videos = 40
total_pages = (total_videos + videos_per_page - 1) // videos_per_page

page = st.number_input("Page", min_value=1, max_value=total_pages, value=1, step=1)

start_index = (page - 1) * videos_per_page + 1
end_index = min(page * videos_per_page + 1, total_videos + 1)

for i in range(start_index, end_index):
    filename = f"prayer {i}.mp4"
    github_url = f"https://raw.githubusercontent.com/formulaglobal/40prayers/main/videos/prayer%20{i}.mp4"

    st.subheader(f"Prayer {i}")
    if filename in descriptions:
        st.write(descriptions[filename])

    st.video(github_url)
    st.markdown(f"[Download {filename}]({github_url})", unsafe_allow_html=True)
    st.markdown("---")

if page == total_pages:
    st.markdown(
        """
        <div style="text-align: center; margin-top: 30px; font-size: 1.1rem; padding: 20px; background-color: #f8f9fa; border-radius: 10px;">
            <p>Get 30 more prayers to attract wealth and prosperity ➡️ 
            <a href="https://lastlink.com/p/C5D1D8C18/checkout-payment/" target="_blank">Click Here</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )
