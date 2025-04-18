import streamlit as st
import os
import json
import re
from PIL import Image
import base64

# Configuração da página
st.set_page_config(
    page_title="40 Prayers to Archangel Michael with FRIAR GILSON",
    page_icon="✨",
    layout="wide",
)

# Estilo customizado
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
    .stDownloadButton button {
        background-color: #FF0000;
        color: white;
        border-radius: 5px;
        padding: 15px 30px;
        font-size: 18px;
        width: 400px;
        margin: 0 auto;
        display: block;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Exibir imagem
image_path = "sao_miguel.jpg"
if os.path.exists(image_path):
    st.image(Image.open(image_path), width=120)
else:
    st.warning("Imagem não encontrada. Verifique o caminho.")

# Título
st.title("40 Prayers to Archangel Michael with FRIAR GILSON")
st.markdown("---")

# Função para extrair o número da oração no nome do arquivo
def extract_number(filename):
    match = re.search(r'prayer\s*(\d+)', filename, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return float('inf')

@st.cache_data(show_spinner=False)
def load_video(video_path):
    with open(video_path, "rb") as file:
        return file.read()

# Carregar e ordenar vídeos
videos = sorted([f for f in os.listdir() if f.endswith(".mp4")], key=extract_number)

# Carregar descrições (opcional)
descriptions = {}
if os.path.exists("descricoes.json"):
    with open("descricoes.json", "r", encoding="utf-8") as f:
        descriptions = json.load(f)

# Exibir os vídeos em ordem de 01 a 40
if not videos:
    st.error("Nenhum vídeo foi encontrado na pasta.")
else:
    st.markdown('<div style="font-size: 0.9rem; color: #666; text-align: center;">Os vídeos estão sendo carregados, aguarde alguns segundos...</div>',
                unsafe_allow_html=True)

    for video in videos:
        st.write(f"### {video}")
        if video in descriptions:
            st.write(descriptions[video])
        video_data = load_video(video)
        video_base64 = base64.b64encode(video_data).decode()
        video_html = f'''
        <div style="display: flex; justify-content: center;">
            <video width="400" controls style="max-width: 100%; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
        '''
        st.markdown(video_html, unsafe_allow_html=True)

        with open(video, "rb") as file:
            st.download_button(
                label=f"Download {video}",
                data=file,
                file_name=video,
                mime="video/mp4",
                key=f"download_{video}",
            )

        st.markdown("---")

# CTA Final
st.markdown(
    """
    <div style="text-align: center; margin-top: 30px; font-size: 1.1rem; padding: 20px; background-color: #f8f9fa; border-radius: 10px;">
        <p>Get 30 more prayers to attract wealth and prosperity ➡️ 
        <a href="https://lastlink.com/p/C5D1D8C18/checkout-payment/" target="_blank">Click Here</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
