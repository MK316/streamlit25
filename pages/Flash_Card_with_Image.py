import streamlit as st
from gtts import gTTS
from io import BytesIO

# --- Flashcard Data ---
flashcards = [
    {
        "word": "Python",
        "pos": "noun",
        "pronunciation": "/ˈpaɪθɑn/",
        "meaning": "A popular programming language known for readability and versatility."
    },
    {
        "word": "forest",
        "pos": "noun",
        "pronunciation": "/ˈfɔːrɪst/",
        "meaning": "A large area covered chiefly with trees and undergrowth."
    },
    {
        "word": "imagine",
        "pos": "verb",
        "pronunciation": "/ɪˈmædʒɪn/",
        "meaning": "To form a mental picture or concept of something not present."
    }
]

# --- GitHub Image URLs for each word (replace with your real links) ---
image_urls = {
    "Python": "https://raw.githubusercontent.com/your-username/your-repo/main/images/python.png",
    "forest": "https://raw.githubusercontent.com/your-username/your-repo/main/images/forest.png",
    "imagine": "https://raw.githubusercontent.com/your-username/your-repo/main/images/imagine.png"
}

# --- Initialize session state ---
if "card_index" not in st.session_state:
    st.session_state.card_index = 0
if "play_audio" not in st.session_state:
    st.session_state.play_audio = True
if "show_image" not in st.session_state:
    st.session_state.show_image = False

# --- Function to go to next flashcard ---
def go_next():
    st.session_state.card_index = (st.session_state.card_index + 1) % len(flashcards)
    st.session_state.play_audio = True
    st.session_state.show_image = False  # reset image on next

# --- Get current flashcard ---
current = flashcards[st.session_state.card_index]

# --- Display the word ---
st.markdown(f"<h1 style='text-align: center; font-size: 60px;'>{current['word']}</h1>", unsafe_allow_html=True)

# --- POS and Pronunciation ---
st.markdown(f"""
<p style='text-align: center; font-size: 22px; color: gray;'>🌱 
    <em>{current['pos']}</em> &nbsp; • &nbsp; <span style='font-family: serif;'>{current['pronunciation']}</span>
</p>
""", unsafe_allow_html=True)

# --- Meaning Box ---
st.markdown(f"""
<div style='padding: 20px; background-color: #f0f8ff; border-left: 6px solid #008cba;
            border-radius: 5px; font-size: 20px; margin-bottom: 30px;'>
    <strong>🎶 Meaning:</strong> {current['meaning']}
</div>
""", unsafe_allow_html=True)

# --- Audio playback (only once when card is loaded) ---
if st.session_state.play_audio:
    tts = gTTS(current["word"])
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    st.audio(audio_fp, format="audio/mp3")
    st.session_state.play_audio = False

# --- Show image button ---
if st.button("🖼️ Show Image"):
    st.session_state.show_image = True

# --- Display image if button clicked ---
if st.session_state.show_image and current["word"] in image_urls:
    st.image(image_urls[current["word"]], use_column_width=True)

# --- Spacer and Next button ---
st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
st.button("➡️ Next", key="next_button", on_click=go_next)

