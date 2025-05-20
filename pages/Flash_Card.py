import streamlit as st

# --- Flashcard data ---
flashcards = [
    {"word": "Python", "meaning": "A popular programming language known for readability and versatility."},
    {"word": "forest", "meaning": "A large area covered chiefly with trees and undergrowth."},
    {"word": "imagine", "meaning": "To form a mental picture or concept of something not present."}
]

# --- Initialize session state ---
if "card_index" not in st.session_state:
    st.session_state.card_index = 0

# --- Handle Next button (must be done before render) ---
def go_next():
    st.session_state.card_index = (st.session_state.card_index + 1) % len(flashcards)

# --- Display flashcard ---
current = flashcards[st.session_state.card_index]
st.markdown(f"<h1 style='text-align: center; font-size: 60px;'>{current['word']}</h1>", unsafe_allow_html=True)

st.markdown(f"""
<div style='padding: 20px; background-color: #f0f8ff; border-left: 6px solid #008cba;
            border-radius: 5px; font-size: 20px; margin-bottom: 30px;'>
    <strong>Meaning:</strong> {current['meaning']}
</div>
""", unsafe_allow_html=True)

# --- Add space and Next button ---
st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
st.button("➡️ Next", key="next_button", on_click=go_next)
