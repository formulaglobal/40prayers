import streamlit as st
import os
import json
import re
from PIL import Image
import base64

# Configuração da página
st.set_page_config(
    page_title="40 Prayers to Archangel Michael",
    page_icon="✨",
    layout="centered",
)

# CSS leve e responsivo
st.markdown(
    """
    <style>
    .stApp { background-color: #f4f4f4; color: #333; }
    h1 {
        color: #4A90E2;
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 1.8rem;
    }
    video {
        width: 100% !important;
        height: auto !important;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    .stDownloadButton button {
        background-color: #FF0000;
        color: white;
        border-radius: 8px;
        font-size: 16px;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Imagem no topo
image_path = "sao_miguel.jpg"
if os.path.exists(image_path):
    st.image(Image.open(image_path), use_column_width=True)
else:
    st.warning("Image not found. Please check the path.")

# Título
st.title("40 Prayers to Archangel Michael with FRIAR GILSON")
st.markdown("---")

# Utilitários
def extract_number(filename):
    match = re.search(r'prayer\s*(\d+)', filename, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return float('inf')

@st.cache_data(show_spinner=False)
def load_video(video_path):
    with open(video_path, "rb") as file:
        return base64.b64encode(file.read()).decode()

# Vídeos
videos = sorted([f for f in os.listdir() if f.endswith(".mp4")], key=extract_number)

# Descrições (se houver)
descriptions = {}
if os.path.exists("descricoes.json"):
    with open("descricoes.json", "r", encoding="utf-8") as f:
        descriptions = json.load(f)

# Quantidade de vídeos por lote
if 'video_count' not in st.session_state:
    st.session_state.video_count = 5

# Exibição
if not videos:
    st.error("No videos found in this folder.")
else:
    st.markdown('<div style="font-size: 0.9rem; color: #666; text-align: center;">Please wait a moment while the content loads...</div>', unsafe_allow_html=True)

    for i, video in enumerate(videos[:st.session_state.video_count]):
        with st.expander(f"▶️ Prayer {i+1:02d} - {video}"):
            if video in descriptions:
                st.write(descriptions[video])
            video_base64 = load_video(video)
            video_html = f'''
            <video controls>
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
            '''
            st.markdown(video_html, unsafe_allow_html=True)

            with open(video, "rb") as file:
                st.download_button(
                    label=f"⬇️ Download Prayer {i+1:02d}",
                    data=file,
                    file_name=video,
                    mime="video/mp4",
                    key=f"download_{video}"
                )
        st.markdown("---")

    # Botão para carregar mais
    if st.session_state.video_count < len(videos):
        if st.button("🔄 Load More Videos"):
            st.session_state.video_count += 5

# CTA final
if st.session_state.video_count >= len(videos):
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px; font-size: 1rem; padding: 15px; background-color: #f8f9fa; border-radius: 10px;">
            <p>Want 30 more powerful prayers to attract wealth and prosperity? ➡️ 
            <a href="https://lastlink.com/p/C5D1D8C18/checkout-payment/" target="_blank">Click here</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )
