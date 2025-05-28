import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


# Функција за анализа
def analyze_audio(filename, color, label):
    try:
        sample_rate, signal = wavfile.read(filename)
        signal = signal[:, 0]  # Лев канал

        # Основна информација
        print(f"\n=== {label} ===")
        print(f"Примероци: {len(signal)}")
        print(f"Времетраење: {len(signal) / sample_rate:.2f} сек")

        # DFT пресметка
        N = len(signal)
        dft = np.fft.fft(signal)
        freqs = np.fft.fftfreq(N, 1 / sample_rate)[:N // 2]
        amps = np.abs(dft)[:N // 2] / N

        # Идентификација на тонови
        notes = {261.63: "C4", 293.66: "D4", 329.63: "E4",
                 349.23: "F4", 392.00: "G4", 440.00: "A4",
                 493.88: "B4", 523.25: "C5"}

        top_peaks = np.argsort(amps)[-3:]  # Топ 3 фреквенции
        print("Најдоминантни фреквенции:")
        for idx in top_peaks:
            freq = freqs[idx]
            closest_note = min(notes.keys(), key=lambda x: abs(x - freq))
            print(f"{freq:.2f} Hz ~ {notes[closest_note]} ({closest_note} Hz)")

        return freqs, amps, color, label

    except FileNotFoundError:
        print(f"Грешка: {filename} не е пронајдена!")
        return None


# Анализа на двата инструменти
flute = analyze_audio('Flejta.wav', 'blue', 'Флејта')
organs = analyze_audio('Orgulji.wav', 'red', 'Оргуљи')

# Визуелизација на споредбата
if flute and organs:
    plt.figure(figsize=(14, 6))

    # Спектар на флејта
    plt.subplot(1, 2, 1)
    plt.plot(flute[0], flute[1], color=flute[2])
    plt.title(f"Спектар: {flute[3]}")
    plt.xlabel("Фреквенција (Hz)")
    plt.ylabel("Амплитуда")
    plt.grid()

    # Спектар на оргуљи
    plt.subplot(1, 2, 2)
    plt.plot(organs[0], organs[1], color=organs[2])
    plt.title(f"Спектар: {organs[3]}")
    plt.xlabel("Фреквенција (Hz)")
    plt.grid()

    # Заеднички споредбен график
    plt.figure(figsize=(12, 6))
    plt.plot(flute[0], flute[1], label=flute[3], alpha=0.7)
    plt.plot(organs[0], organs[1], label=organs[3], alpha=0.7)
    plt.title("Споредба на спектри")
    plt.xlabel("Фреквенција (Hz)")
    plt.ylabel("Амплитуда")
    plt.legend()
    plt.grid()
    plt.show()