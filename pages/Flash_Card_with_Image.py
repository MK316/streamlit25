import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO

# --- Load data from CSV ---
@st.cache_data
def load_flashcards():
    return pd.read_csv("https://raw.githubusercontent.com/MK316/streamlit25/refs/heads/main/data/flashcard.csv")  # adjust path if needed

df = load_flashcards()

# --- Initialize session state ---
if "card_index" not in st.session_state:
    st.session_state.card_index = 0
if "play_audio" not in st.session_state:
    st.session_state.play_audio = True
if "show_image" not in st.session_state:
    st.session_state.show_image = False

# --- Go to next card ---
def go_next():
    st.session_state.card_index = (st.session_state.card_index + 1) % len(df)
    st.session_state.play_audio = True
    st.session_state.show_image = False

# --- Current flashcard data ---
current = df.iloc[st.session_state.card_index]
word = current["Word"]
pos = current["POS"]
pron = current["Pronunciation"]
meaning = current.get("Meaning", "📝 No meaning provided.")
image_url = current["Image"]

# --- Display word ---
st.markdown(f"<h1 style='text-align: center; font-size: 60px;'>{word}</h1>", unsafe_allow_html=True)

# --- POS & Pronunciation ---
st.markdown(f"""
<p style='text-align: center; font-size: 22px; color: gray;'>🌱 
    <em>{pos}</em> &nbsp; • &nbsp; <span style='font-family: serif;'>{pron}</span>
</p>
""", unsafe_allow_html=True)

# --- Meaning ---
st.markdown(f"""
<div style='padding: 20px; background-color: #f0f8ff; border-left: 6px solid #008cba;
            border-radius: 5px; font-size: 20px; margin-bottom: 30px;'>
    <strong>🎶 Meaning:</strong> {meaning}
</div>
""", unsafe_allow_html=True)

# --- Audio playback ---
if st.session_state.play_audio:
    tts = gTTS(word)
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    st.audio(audio_fp, format="audio/mp3")
    st.session_state.play_audio = False

# --- Show image button ---
if st.button("🖼️ Show Image"):
    st.session_state.show_image = True

# --- Display image ---
if st.session_state.show_image:
    st.image(image_url, use_container_width=True)

# --- Next button ---
st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
st.button("➡️ Next", key="next_button", on_click=go_next)
