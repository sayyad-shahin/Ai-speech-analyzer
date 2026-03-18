from src.recorder import record_audio
from src.feature_extractor import extract_features
from src.analyzer import analyze_voice
from src.tts import speak

def main():
    # Step 1: Record audio
    record_audio()

    # Step 2: Extract features
    pitch, freq, energy = extract_features("audio/input.wav")

    # Step 3: Analyze
    pitch_type, emotion = analyze_voice(pitch, freq, energy)

    # Step 4: Print result
    print("\n===== RESULT =====")
    print("Pitch:", pitch)
    print("Frequency:", freq)
    print("Energy:", energy)
    print("Type:", pitch_type)
    print("Emotion:", emotion)

    # Step 5: Voice output
    speak(f"Your voice is {pitch_type} and {emotion}")

if __name__ == "__main__":
    main()