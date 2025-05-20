import streamlit as st

# --- Sample flashcards ---
flashcards = [
    {"word": "Python", "meaning": "A popular programming language known for readability and versatility."},
    {"word": "forest", "meaning": "A large area covered chiefly with trees and undergrowth."},
    {"word": "imagine", "meaning": "To form a mental picture or concept of something not present."}
]

# --- Initialize session state ---
if "card_index" not in st.session_state:
    st.session_state.card_index = 0

# --- Display current flashcard ---
current = flashcards[st.session_state.card_index]
st.markdown(f"<h1 style='text-align: center; font-size: 60px;'>{current['word']}</h1>", unsafe_allow_html=True)

st.markdown(f"""
<div style='padding: 20px; background-color: #f0f8ff; border-left: 6px solid #008cba; border-radius: 5px; font-size: 20px;'>
    <strong>Meaning:</strong> {current['meaning']}
</div>
""", unsafe_allow_html=True)

# --- Next button ---
if st.button("➡️ Next"):
    st.session_state.card_index += 1
    if st.session_state.card_index >= len(flashcards):
        st.session_state.card_index = 0  # Loop back to start
