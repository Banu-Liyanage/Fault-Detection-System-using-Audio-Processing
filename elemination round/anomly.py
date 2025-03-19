import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import os
import glob


# Function to extract MFCC features
def extract_features(file_path, n_mfcc=13):
    y, sr = librosa.load(file_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return np.mean(mfccs, axis=1)


# Load normal training sounds
normal_sound_files = glob.glob("data/normal/*.wav")
normal_features = np.array([extract_features(f) for f in normal_sound_files])

# Scale features
scaler = StandardScaler()
normal_features_scaled = scaler.fit_transform(normal_features)

# Train an Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(normal_features_scaled)


# Function to predict anomalies
def predict_anomaly(file_path):
    feature = extract_features(file_path).reshape(1, -1)
    feature_scaled = scaler.transform(feature)
    pred = model.predict(feature_scaled)
    return "Anomaly" if pred[0] == -1 else "Normal"


# Test on new data
test_files = glob.glob("data/test/*.wav")
for file in test_files:
    print(f"{file}: {predict_anomaly(file)}")
