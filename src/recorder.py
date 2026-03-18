import sounddevice as sd
from scipy.io.wavfile import write
import os

def list_devices():
    print("\nAvailable Audio Devices:")
    print(sd.query_devices())

def record_audio(filename="audio/input.wav", duration=5, fs=44100, device=None):
    try:
        # Create audio folder if not exists
        os.makedirs("audio", exist_ok=True)

        print("\n🎤 Recording will start...")
        print(f"Duration: {duration} seconds")

        if device is not None:
            print(f"Using device ID: {device}")

        # Record audio
        audio = sd.rec(
            int(duration * fs),
            samplerate=fs,
            channels=1,
            dtype='int16',   # better compatibility
            device=device    # select mic (optional)
        )

        sd.wait()

        # Save file
        write(filename, fs, audio)

        print(f"✅ Audio saved at: {filename}")

    except Exception as e:
        print("❌ Error during recording:", str(e))