import os
import numpy as np
from src.feature_extractor import extract_features

def load_data(dataset_path):
    X, y = [], []

    for root, _, files in os.walk(dataset_path):
        for file in files:
            if file.endswith(".wav"):
                path = os.path.join(root, file)

                # RAVDESS label
                emotion = file.split("-")[2]

                features = extract_features(path)

                X.append(features)
                y.append(emotion)

    return np.array(X), np.array(y)