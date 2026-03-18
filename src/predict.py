import joblib
from src.feature_extractor import extract_features

model = joblib.load("model.pkl")

# Emotion mapping
emotion_map = {
    "01": "Neutral",
    "02": "Calm",
    "03": "Happy",
    "04": "Sad",
    "05": "Angry",
    "06": "Fear",
    "07": "Disgust",
    "08": "Surprise"
}

def predict_all(file_path):
    mfcc, pitch, freq, energy = extract_features(file_path)

    prediction = model.predict(mfcc.reshape(1, -1))[0]
    emotion = emotion_map.get(prediction, "Unknown")

    # Pitch type
    pitch_type = "High Pitch" if pitch > 180 else "Low Pitch"

    # Frequency type
    freq_type = "High Frequency" if freq > 2000 else "Low Frequency"

    return emotion, pitch, freq, energy, pitch_type, freq_type