import librosa
import numpy as np

def extract_features(file_path):
    # Load audio
    audio, sr = librosa.load(file_path, duration=3)

    # =========================
    # MFCC (for model)
    # =========================
    mfcc = np.mean(librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13).T, axis=0)

    # =========================
    # IMPROVED PITCH DETECTION
    # =========================
    pitches, magnitudes = librosa.piptrack(y=audio, sr=sr)

    pitch_values = []

    for i in range(pitches.shape[1]):
        index = magnitudes[:, i].argmax()
        pitch = pitches[index, i]

        # Filter realistic human pitch range
        if 50 < pitch < 400:
            pitch_values.append(pitch)

    if len(pitch_values) > 0:
        pitch = np.mean(pitch_values)
    else:
        pitch = 0  # fallback if no valid pitch

    # =========================
    # FREQUENCY (CLEANED)
    # =========================
    freq = np.mean(librosa.feature.spectral_centroid(y=audio, sr=sr))

    # Clamp unrealistic values
    if freq > 4000:
        freq = 4000

    # =========================
    # ENERGY
    # =========================
    energy = np.mean(librosa.feature.rms(y=audio))

    return mfcc, pitch, freq, energy