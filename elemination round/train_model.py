import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


def train_model(features, model_name):
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(features_scaled)

    joblib.dump(model, f"models/{model_name}_model.pkl")
    joblib.dump(scaler, f"models/{model_name}_scaler.pkl")


# Load extracted features
bearing_train = joblib.load("models/bearing_features.pkl")
gearbox_train = joblib.load("models/gearbox_features.pkl")
fan_train = joblib.load("models/fan_features.pkl")

# Train and save models
train_model(bearing_train, "bearing")
train_model(gearbox_train, "gearbox")
train_model(fan_train, "fan")

print("Model training complete!")
