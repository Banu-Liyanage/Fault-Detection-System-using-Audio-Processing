import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from pydub import AudioSegment
import os


def convert_mp3_to_wav(mp3_file):
    """Convert MP3 to WAV using pydub and return the WAV filename"""
    wav_file = mp3_file.replace(".mp3", ".wav")
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format="wav")
    return wav_file


def plot_fft(audio_file):
    """Read an audio file, compute FFT, and plot the frequency spectrum"""

    # Convert MP3 to WAV if needed
    if audio_file.lower().endswith(".mp3"):
        print(f"Converting {audio_file} to WAV...")
        audio_file = convert_mp3_to_wav(audio_file)

    # Read the audio file
    sample_rate, data = wavfile.read(audio_file)

    # Convert to mono if stereo
    if len(data.shape) > 1:
        data = data.mean(axis=1)

    # Perform FFT
    N = len(data)
    fft_output = np.fft.fft(data)
    freqs = np.fft.fftfreq(N, 1 / sample_rate)

    # Take only the positive half of the spectrum
    half_N = N // 2
    freqs = freqs[:half_N]
    magnitude = np.abs(fft_output[:half_N])

    # Plot FFT
    plt.figure(figsize=(10, 5))
    plt.plot(freqs, magnitude, color="blue", label=audio_file)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title
    plt.legend()
    plt.grid()
    plt.show()


plot_fft(r"C:\Users\Cyborg\Desktop\SLIOT\gearbox.mp3")
