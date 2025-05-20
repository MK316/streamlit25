import streamlit as st

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

# --- Session State ---
if "card_index" not in st.session_state:
    st.session_state.card_index = 0

# --- Navigation ---
def go_next():
    st.session_state.card_index = (st.session_state.card_index + 1) % len(flashcards)

# --- Current Flashcard ---
current = flashcards[st.session_state.card_index]

# --- Display Word ---
st.markdown(f"<h1 style='text-align: center; font-size: 60px;'>{current['word']}</h1>", unsafe_allow_html=True)

# --- POS and Pronunciation ---
st.markdown(f"""
<p style='text-align: center; font-size: 22px; color: gray;'>
    <em>{current['pos']}</em> &nbsp; • &nbsp; <span style='font-family: serif;'>{current['pronunciation']}</span>
</p>
""", unsafe_allow_html=True)

# --- Meaning ---
st.markdown(f"""
<div style='padding: 20px; background-color: #f0f8ff; border-left: 6px solid #008cba;
            border-radius: 5px; font-size: 20px; margin-bottom: 30px;'>
    <strong>Meaning:</strong> {current['meaning']}
</div>
""", unsafe_allow_html=True)

# --- Navigation Button ---
st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
st.button("➡️ Next", key="next_button", on_click=go_next)
