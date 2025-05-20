import streamlit as st
from gtts import gTTS
from io import BytesIO

# --- Sentences to dictate ---
sentences = [
    "The sun is shining brightly.",
    "She goes to school every morning.",
    "Can you help me carry these books?"
]

# --- Initialize session state ---
if "index" not in st.session_state:
    st.session_state.index = 0
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "show_audio" not in st.session_state:
    st.session_state.show_audio = True

st.title("🎧 Dictation Practice")
st.markdown("Listen to the sentence and type exactly what you hear, including **punctuation** and **capitalization**.")

# --- Stop when all sentences are done ---
if st.session_state.index >= len(sentences):
    st.success("✅ You’ve completed all the sentences!")
    if st.button("🔄 Start Over"):
        st.session_state.index = 0
        st.session_state.user_input = ""
        st.session_state.submitted = False
        st.session_state.show_audio = True
    st.stop()

# --- Get current sentence ---
current_sentence = sentences[st.session_state.index]

# --- Only generate and play audio when needed ---
if st.session_state.show_audio:
    tts = gTTS(current_sentence)
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    st.audio(audio_fp, format="audio/mp3")
    st.session_state.show_audio = False  # prevent re-generating unless next sentence

# --- Input box that retains text ---
st.session_state.user_input = st.text_input("Type what you heard:", value=st.session_state.user_input)

# --- Submit and check answer ---
if st.button("✅ Submit"):
    st.session_state.submitted = True
    if st.session_state.user_input.strip() == current_sentence:
        st.success("✅ Correct!")
        st.session_state.index += 1
        st.session_state.user_input = ""
        st.session_state.submitted = False
        st.session_state.show_audio = True  # allow next sentence audio
    else:
        st.error("❌ There's a mistake. Please check your grammar and punctuation.")

# --- Replay button ---
if st.button("🔁 Replay Audio"):
    st.session_state.show_audio = True
