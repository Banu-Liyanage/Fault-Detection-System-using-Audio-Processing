
# Smart Fault Detection 🔊

An intelligent acoustic monitoring system for **industrial machinery fault detection** using **machine learning**.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub issues](https://img.shields.io/github/issues/yourusername/smart-fault-detection)](https://github.com/yourusername/smart-fault-detection/issues)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/smart-fault-detection)](https://github.com/yourusername/smart-fault-detection/stargazers)

---

## 🚀 Overview

This project leverages machine learning techniques to **detect anomalies in industrial machines** by analyzing their acoustic signatures. Our system can classify **normal vs faulty conditions** and identify anomalies in real-time. 

✅ **Key Technologies:** Librosa, Scikit-learn, Isolation Forest, FastAPI, FFT, MFCC, ESP32 (for IoT integration).

✅ **Challenge:** Developed for the **SLIOT Challenge** organized by the **Department of CSE, University of Moratuwa**.

✅ **Goal:** Early fault detection to **prevent machine failures** and **reduce maintenance costs**.

---

## 🔥 Features

- 🎤 **Real-time sound recording** - Capture and analyze machine noise in real-time.
- 📊 **Feature extraction** - Extract **MFCCs**, **FFT**, **Spectrograms**, and other acoustic features.
- 🤖 **AI-based fault detection** - Uses **Isolation Forest** for unsupervised anomaly detection.
- 🌍 **IoT integration** - Deployable on **ESP32** for real-time monitoring.
- ⚡ **Fast and lightweight** - Optimized for **low-latency** edge devices.
- 📈 **Jupyter Notebooks** - Includes interactive data analysis and model training.

---

## 🛠 Installation

### 1️⃣ Prerequisites
- Python **3.8+**
- Git
- Virtual environment (recommended: venv/conda)
- Audio recording device
- (Optional) **CUDA-compatible GPU** for faster training

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/smart-fault-detection.git
cd smart-fault-detection
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Settings
```bash
cp config/settings.example.yaml config/settings.yaml
# Edit settings.yaml as needed
```

---

## 🎤 Data Collection

The system supports **real-time recording** and **pre-recorded audio**:
- Store raw audio files in **data/raw/**
- Processed features are saved in **data/processed/**
- Default **sample rate:** 44.1 kHz (configurable in settings)
- Recommended **clip length:** 3-5 seconds

### Recording a Sample
```bash
python src/record_audio.py --output data/raw/sample.wav
```

---

## 🚀 Usage

### 1️⃣ Extract Features (MFCC & FFT)
```bash
python src/feature_extraction.py
```

### 2️⃣ Train the Machine Learning Model
```bash
python src/train_model.py
```

### 3️⃣ Test the Model
```bash
python src/test_model.py
```

### 4️⃣ Predict Faults on New Data
```bash
python src/predict_fault.py --input test_audio.wav
```

### 5️⃣ Deploy the Real-Time Fault Detection API
```bash
python app/main.py
```
Access the API at: **http://localhost:5000/predict**

---

## 🧪 Testing
To ensure everything works, run:
```bash
pytest tests/
```

---

## 📁 Project Structure

```
smart-fault-detection/
├── app/                    # API implementation
├── config/                 # Configuration files
├── data/                   # Dataset storage
│   ├── raw/                # Raw audio recordings
│   └── processed/          # Processed features
├── models/                 # Trained models
├── notebooks/              # Jupyter notebooks
├── src/                    # Source code
│   ├── features/           # Feature extraction (MFCC, FFT)
│   ├── models/             # Machine learning models
│   ├── data/               # Data processing utilities
│   ├── visualization/      # Plotting utilities
├── tests/                  # Unit tests
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 📈 Model Training Pipeline

1. **Data Collection** - Gather machine sounds
2. **Preprocessing** - Normalize and clean data
3. **Feature Extraction** - Compute **MFCCs**, **FFT**, **Zero-Crossing Rate**, etc.
4. **Training** - Train **Isolation Forest** or other ML models
5. **Evaluation** - Test accuracy & fine-tune parameters
6. **Deployment** - Deploy as **API** or integrate with **IoT devices**

---

## 🏗 Future Improvements

🔥 **Deep Learning Integration** - Improve accuracy with CNNs and LSTMs  
🌎 **IoT Deployment** - Real-time edge processing on **ESP32, Raspberry Pi**  
📊 **Web Dashboard** - Live fault visualization  
⚙️ **Optimized for Embedded Systems** - Faster and power-efficient models  

---

## 👥 Contributing

Contributions are welcome! Follow these steps:
1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature-name`)
3. **Commit your changes** (`git commit -m 'Added feature XYZ'`)
4. **Push to your branch** (`git push origin feature-name`)
5. **Submit a Pull Request** 🎉

---

## 📜 License

This project is licensed under the **MIT License** - see the **LICENSE** file for details.

---

## 📞 Contact

**Your Name** - @yourusername - email@example.com  
📌 **Project Link:** [GitHub Repo](https://github.com/yourusername/smart-fault-detection)
```

You can copy and save this as `README.md` in your project directory. Let me know if you need further refinements! 🚀
