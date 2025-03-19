import librosa
import numpy as np
import glob
import joblib


def extract_mfcc(file_path, n_mfcc=13):
    y, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return np.mean(mfcc, axis=1)


def process_dataset(dataset_path):
    files = glob.glob(f"{dataset_path}/*.wav")
    features = np.array([extract_mfcc(f) for f in files])
    return features


# Extract and save features
bearing_train = process_dataset("data/bearing/train")
joblib.dump(bearing_train, "models/bearing_features.pkl")

gearbox_train = process_dataset("data/gearbox/train")
joblib.dump(gearbox_train, "models/gearbox_features.pkl")

fan_train = process_dataset("data/fan/train")
joblib.dump(fan_train, "models/fan_features.pkl")

print("Feature extraction complete!")
