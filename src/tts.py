import pyttsx3

def generate_audio(text, output_file="audio/output.wav"):
    engine = pyttsx3.init()

    # Optional: control voice speed
    engine.setProperty('rate', 150)

    engine.save_to_file(text, output_file)
    engine.runAndWait()

    return output_file