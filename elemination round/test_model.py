import joblib
import glob
import numpy as np
from MFCC import extract_mfcc


def detect_anomalies(model_name, test_path):
    model = joblib.load(f"models/{model_name}_model.pkl")
    scaler = joblib.load(f"models/{model_name}_scaler.pkl")

    test_files = glob.glob(f"{test_path}/*.wav")
    results = []

    for file in test_files:
        feature = extract_mfcc(file).reshape(1, -1)
        feature_scaled = scaler.transform(feature)
        pred = model.predict(feature_scaled)
        result = "Anomaly" if pred[0] == -1 else "Normal"
        results.append((file, result))

    return results


# Run anomaly detection on test sets
bearing_results = detect_anomalies("bearing", "data/bearing/test")
gearbox_results = detect_anomalies("gearbox", "data/gearbox/test")
fan_results = detect_anomalies("fan", "data/fan/test")

# Print results
for res in bearing_results[:50]:
    print(f"Bearing - {res}")

for res in gearbox_results[:50]:
    print(f"Gearbox - {res}")

for res in fan_results[:50]:
    print(f"Fan - {res}")
