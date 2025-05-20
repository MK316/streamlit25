import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO

# --- Load CSV from GitHub ---
@st.cache_data
def load_flashcards():
    url = "https://raw.githubusercontent.com/MK316/streamlit25/main/data/flashcard.csv"
    df = pd.read_csv(url, quotechar='"')
    df.columns = df.columns.str.strip()  # remove whitespace from column names
    return df

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

# --- Get current card data ---
current = df.iloc[st.session_state.card_index]
word = current["Word"]
pos = current["POS"]
pron = current["Pronunciation"]
meaning = current["Meaning"]
image_url = current["Image"]

# --- Display word ---
st.markdown(f"<h1 style='text-align: center; font-size: 60px;'>{word}</h1>", unsafe_allow_html=True)

# --- POS & Pronunciation ---
st.markdown(f"""
<p style='text-align: center; font-size: 22px; color: gray;'>🌱 
    <em>{pos}</em> &nbsp; • &nbsp; <span style='font-family: serif;'>{pron}</span>
</p>
""", unsafe_allow_html=True)

# --- Meaning Box ---
st.markdown(f"""
<div style='padding: 20px; background-color: #f0f8ff; border-left: 6px solid #008cba;
            border-radius: 5px; font-size: 20px; margin-bottom: 30px;'>
    <strong>🎶 Meaning:</strong> {meaning}
</div>
""", unsafe_allow_html=True)

# --- Play audio once per card load ---
if st.session_state.play_audio:
    tts = gTTS(word)
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    st.audio(audio_fp, format="audio/mp3")
    st.session_state.play_audio = False

# --- Next Button ---
st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
st.button("➡️ Next", key="next_button", on_click=go_next)

# --- Show image button ---
if st.button("🖼️ Show Image"):
    st.session_state.show_image = True

# --- Display image if triggered ---
if st.session_state.show_image:
    st.image(image_url, width=300)


