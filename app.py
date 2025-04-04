import base64

import streamlit as st
import os
import json
import re
from PIL import Image

# Load users from JSON
USERS_FILE = "users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def register_user():
    st.subheader("Create an Account")
    username = st.text_input("Choose a username", key="new_user")
    password = st.text_input("Choose a password", type="password", key="new_pass")
    email = st.text_input("Email (for password recovery)", key="new_email")

    if st.button("Register"):
        users = load_users()
        if username in users:
            st.error("Username already exists.")
        elif not username or not password or not email:
            st.error("All fields are required.")
        else:
            users[username] = {"password": password, "email": email}
            save_users(users)
            st.success("Account created! You can now log in.")

def forgot_password():
    st.subheader("Recover Password")
    email = st.text_input("Enter your email")

    if st.button("Recover"):
        users = load_users()
        for user, data in users.items():
            if data.get("email") == email:
                st.info(f"User found: **{user}**, your password is: **{data['password']}**")
                return
        st.error("Email not found.")

def login():
    st.subheader("Login")
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")

    if st.button("Login"):
        users = load_users()
        if username in users and users[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.error("Invalid username or password.")

def auth_flow():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        option = st.radio("Access Option", ["Login", "Register", "Forgot Password"])
        if option == "Login":
            login()
        elif option == "Register":
            register_user()
        elif option == "Forgot Password":
            forgot_password()
        st.stop()

# Run authentication
auth_flow()

# ------------------- Main App Content -------------------

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

# Image on top
image_path = "sao_miguel.jpg"
if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, width=120)
else:
    st.warning("Image not found. Please check the path.")

# Title
st.title("40 Prayers to Archangel Michael with FRIAR GILSON")
st.markdown("---")

# Load videos
def extract_number(filename):
    match = re.search(r'prayer\s*(\d+)', filename, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return float('inf')

@st.cache_data(show_spinner=False)
def load_video(video_path):
    with open(video_path, "rb") as file:
        return file.read()

videos = sorted([f for f in os.listdir() if f.endswith(".mp4")], key=extract_number)

# Load descriptions
descriptions = {}
if os.path.exists("descricoes.json"):
    with open("descricoes.json", "r", encoding="utf-8") as f:
        descriptions = json.load(f)

if not videos:
    st.error("No videos found in the current folder.")
else:
    st.write("### Choose a prayer to watch:")
    st.markdown('<div style="font-size: 0.9rem; color: #666; text-align: center;">Please wait a few seconds for the videos to load...</div>',
                unsafe_allow_html=True)

    for i, video in enumerate(videos):
        st.write(f"**{video}**")
        if video in descriptions:
            st.write(descriptions[video])
        video_data = load_video(video)
        
        video_base64 = base64.b64encode(video_data).decode()
        video_html = f"""
        <div style='display: flex; justify-content: center;'>
            <video width='400' controls style='max-width: 100%; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);'>
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
        """
        st.markdown(video_html, unsafe_allow_html=True)

        with open(video, "rb") as file:
            st.download_button(
                label=f"Download {video}",
                data=file,
                file_name=video,
                mime="video/mp4",
                key=f"download_{video}",
            )
        if i == len(videos) - 1:
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
