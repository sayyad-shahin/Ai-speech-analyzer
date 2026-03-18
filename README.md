AI Speech Analyzer

AI Speech Analyzer is a Python project for detecting emotions from audio recordings. It extracts features like MFCCs, pitch, frequency, and energy, and uses machine learning to predict emotions. The system includes a Streamlit UI for uploading audio files and visualizing results.

Features

Upload .wav or .mp3 audio files

Audio preprocessing using Librosa

Feature extraction: MFCC, pitch, frequency, energy

Emotion detection with Random Forest

Visual results and analysis in Streamlit UI

Installation

Clone the repository:

git clone https://github.com/sayyad-shahin/Ai-speech-analyzer.git
cd Ai-speech-analyzer

Create a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
Usage

Run the Streamlit app:

streamlit run streamlit_app.py

Open the URL shown in the terminal to interact with the app, upload audio files, and see emotion predictions.

Supported Emotions

Happy

Sad

Angry

Neutral

Fearful

Surprised

(Based on RAVDESS dataset labeling.)

Project Structure
AI-Voice-Analyzer/
├── streamlit_app.py       # Streamlit UI
├── src/                   # Audio processing and ML code
├── data/                  # Example audio files / datasets
├── requirements.txt
└── README.md
Tech Stack

Python

Librosa

scikit-learn (Random Forest)

Streamlit

Dataset

Uses RAVDESS dataset for labeled audio emotion detection: RAVDESS Dataset

Future Improvements

Add Text-to-Speech (TTS) for real-time testing

Integrate deep learning models for better accuracy

Expand supported emotions and multilingual support

License

MIT License – open-source project
