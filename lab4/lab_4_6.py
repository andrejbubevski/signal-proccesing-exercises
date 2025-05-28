import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import os

def plot_spectrum(signal, sample_rate, title):
    N = len(signal)
    spectrum = np.fft.fft(signal)
    freqs = np.fft.fftfreq(N, d=1/sample_rate)
    half = N // 2

    plt.figure(figsize=(10, 4))
    plt.plot(freqs[:half], np.abs(spectrum[:half]), color='darkblue')
    plt.title(f'Амплитуден спектар - {title}')
    plt.xlabel('Фреквенција [Hz]')
    plt.ylabel('Амплитуда')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_segments(signal, sample_rate, window_size, hop_size, title):
    N = len(signal)
    segment_num = 1

    for start in range(0, N - window_size, hop_size):
        segment = signal[start:start + window_size]
        spectrum = np.fft.fft(segment)
        freqs = np.fft.fftfreq(window_size, d=1/sample_rate)
        half = window_size // 2

        plt.figure(figsize=(8, 3))
        plt.plot(freqs[:half], np.abs(spectrum[:half]), color='green')
        plt.title(f'Segment {segment_num} ({start} - {start + window_size}) - {title}')
        plt.xlabel('Фреквенција [Hz]')
        plt.xlim(0, 1800)
        plt.ylabel('Амплитуда')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        segment_num += 1

def analyze_file(file_path, title):
    print(f"--- Анализа на {title} ---")
    if not os.path.exists(file_path):
        print(f"Фајлот '{file_path}' не постои.")
        return

    sample_rate, data = wavfile.read(file_path)
    signal = data[:, 0]  # само првиот канал
    print(f"Sample rate: {sample_rate} Hz | Должина на сигналот: {len(signal)} примероци")

    plot_spectrum(signal, sample_rate, title)
    plot_segments(signal, sample_rate, window_size=2048, hop_size=8000, title=title)

# Анализа на флејта и оргуљи
analyze_file("Flejta.wav", "Флејта")
#analyze_file("Orgulji.wav", "Оргуљи")
