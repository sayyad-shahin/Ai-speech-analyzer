def analyze_voice(pitch, frequency, energy):

    if pitch < 150:
        pitch_type = "Low Pitch"
    elif pitch < 300:
        pitch_type = "Medium Pitch"
    else:
        pitch_type = "High Pitch"

    if energy > 0.1:
        emotion = "Energetic"
    else:
        emotion = "Calm"

    return pitch_type, emotion