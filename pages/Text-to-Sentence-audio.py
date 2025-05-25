import streamlit as st
from gtts import gTTS
import re
from io import BytesIO

st.title("🗣️ Sentence-by-Sentence Text-to-Speech")

# --- Input area ---
text = st.text_area("✍️ Enter your text below:", height=200)

if st.button("🔊 Generate Sentence Audio"):
    if text.strip():
        # Step 1: Split into sentences
        sentences = re.split(r'(?<=[.!?]) +', text.strip())

        st.info(f"{len(sentences)} sentence(s) found.")

        # Step 2: Generate and play each sentence
        for i, sentence in enumerate(sentences, 1):
            st.markdown(f"**Sentence {i}:** {sentence}")
            tts = gTTS(sentence, lang='en')
            mp3_fp = BytesIO()
            tts.write_to_fp(mp3_fp)
            st.audio(mp3_fp.getvalue(), format='audio/mp3')
    else:
        st.warning("Please enter some text to convert.")
