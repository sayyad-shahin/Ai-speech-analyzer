import streamlit as st
import os

from src.feature_extractor import extract_features
from src.analyzer import analyze_voice
from src.tts import generate_audio

st.set_page_config(page_title="AI Voice Emotion Analyzer", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'> AI Voice Emotion Analyzer</h1>", unsafe_allow_html=True)

st.write("Upload an audio file (.wav or .mp3) to analyze voice properties")

# File Upload
uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])

if uploaded_file is not None:
    os.makedirs("audio", exist_ok=True)

    file_path = os.path.join("audio", uploaded_file.name)

    # Save file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ File uploaded successfully!")

    # Play audio
    st.audio(file_path)

    # =========================
    # FEATURE EXTRACTION
    # =========================
    mfcc, pitch, freq, energy = extract_features(file_path)

    # =========================
    # ANALYSIS
    # =========================
    pitch_type, emotion = analyze_voice(pitch, freq, energy)

    # =========================
    # DISPLAY RESULTS
    # =========================
    st.markdown("###  Analysis Result")

    st.write(f" Emotion: **{emotion}**")
    st.write(f" Pitch Value: **{pitch:.2f}**")
    st.write(f" Frequency: **{freq:.2f} Hz**")
    st.write(f" Energy: **{energy:.4f}**")
    st.write(f" Pitch Type: **{pitch_type}**")

    # Frequency category
    if freq > 2000:
        st.write(" Frequency Type: **High Frequency**")
    else:
        st.write(" Frequency Type: **Low Frequency**")
    
    # =========================
    # GENERATE OUTPUT AUDIO
    # =========================
    output_text = f"The emotion is {emotion}. The pitch is {pitch_type} and the frequency is {'high' if freq > 2000 else 'low'}."
    
    output_file = generate_audio(output_text)
    
    st.markdown("###  Generated Voice Output")
    
    # Play generated audio
    st.audio(output_file)
    
    # Download button
    with open(output_file, "rb") as f:
        st.download_button(
            label="⬇️ Download Audio Result",
            data=f,
            file_name="voice_analysis.wav",
            mime="audio/wav"
        )