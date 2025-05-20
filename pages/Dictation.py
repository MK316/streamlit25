import streamlit as st
from gtts import gTTS
from io import BytesIO

# --- List of sentences for dictation ---
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
if "replay_audio" not in st.session_state:
    st.session_state.replay_audio = True  # Play first audio on load

# --- Title and Instructions ---
st.title("🎧 Dictation Practice")
st.markdown("Listen to the sentence and type exactly what you hear, including **punctuation** and **capitalization**.")

# --- End of all sentences ---
if st.session_state.index >= len(sentences):
    st.success("✅ You’ve completed all the sentences!")
    if st.button("🔄 Start Over"):
        st.session_state.index = 0
        st.session_state.user_input = ""
        st.session_state.submitted = False
        st.session_state.replay_audio = True
    st.stop()

# --- Get current sentence ---
current_sentence = sentences[st.session_state.index]

# --- Generate and play audio (only if flag is True) ---
if st.session_state.replay_audio:
    tts = gTTS(current_sentence)
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    st.audio(audio_fp, format="audio/mp3")
    st.session_state.replay_audio = False

# --- Replay Audio Button ---
if st.button("🔁 Replay Audio"):
    st.session_state.replay_audio = True

# --- Input box that retains previous input ---
st.session_state.user_input = st.text_input(
    "✏️ Type what you heard:", value=st.session_state.user_input
)

# --- Submit Button and Answer Check ---
if st.button("✅ Submit"):
    st.session_state.submitted = True
    if st.session_state.user_input.strip() == current_sentence:
        st.success("✅ Correct!")
        st.session_state.index += 1
        st.session_state.user_input = ""
        st.session_state.submitted = False
        st.session_state.replay_audio = True
    else:
        st.error("❌ Not quite. Check your spelling, punctuation, and capitalization.")


st.markdown("---")
st.markdown("[App code to copy](https://github.com/MK316/streamlit25/blob/main/pages/Dictation.py)")
