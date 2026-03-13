import streamlit as st
from gtts import gTTS
import os

def read_aloud(text):
    """Simple TTS for Frank's response."""
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("response.mp3")
    st.audio("response.mp3", format="audio/mp3", autoplay=True)

# For Voice Record, we will use the streamlit-mic-recorder component in app.py