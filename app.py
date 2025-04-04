
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

# Custom CSS
st.markdown(
    """
    <style>
    .stApp { background-color: #f4f4f4; color: #333; }
    h1 {
        color: #4A90E2;
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 2.5rem;
    }
    .stButton button {
        background-color: #4A90E2;
        color: white;
        border-radius: 5px;
        padding: 15px 30px;
        font-size: 18px;
        font-family: 'Georgia', serif;
        width: 100%;
    }
    .stDownloadButton button {
        background-color: #FF0000;
        color: white;
        border-radius: 5px;
        padding: 15px 30px;
        font-size: 18px;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display top image
image_path = "sao_miguel.jpg"
if os.path.exists(image_path):
    st.image(image_path, width=120)
else:
    st.warning("Image not found. Please check the path.")

st.title("40 Prayers to Archangel Michael with FRIAR GILSON")
st.markdown("---")

# Load descriptions if available
descriptions = {}
if os.path.exists("descricoes.json"):
    with open("descricoes.json", "r", encoding="utf-8") as f:
        descriptions = json.load(f)

# Render GitHub-hosted videos
for i in range(1, 41):
    filename = f"prayer {i}.mp4"
    st.write(f"**{filename}**")
    
    if filename in descriptions:
        st.write(descriptions[filename])
    
    github_url = f"https://raw.githubusercontent.com/formulaglobal/40prayers/main/videos/prayer%20{i}.mp4"
    st.video(github_url)
    st.markdown(f"[Download {filename}]({github_url})", unsafe_allow_html=True)

    if i == 40:
        st.markdown("---")
        st.markdown(
            """
            <div style="text-align: center; margin-top: 30px; font-size: 1.1rem; padding: 20px; background-color: #f8f9fa; border-radius: 10px;">
                <p>Get 30 more prayers to attract wealth and prosperity ➡️ 
                <a href="https://lastlink.com/p/C5D1D8C18/checkout-payment/" target="_blank">Click Here</a></p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown("---")
