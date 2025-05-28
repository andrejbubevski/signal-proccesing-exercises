import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Вчитување на сигналот
sample_rate, signal = wavfile.read('Flejta.wav')
signal = signal[:, 0]  # Само левиот канал
N = len(signal)
duration = N / sample_rate

# Основна информација
print(f"Фреквенција на семплирање: {sample_rate} Hz")
print(f"Број на примероци: {N}")
print(f"Времетраење: {duration:.2f} секунди")

# Пресметка на DFT
dft = np.fft.fft(signal)
freqs = np.fft.fftfreq(N, 1/sample_rate)
amplitudes = np.abs(dft) / N  # Нормализација

# Приказ на амплитудниот спектар
plt.figure(figsize=(12, 6))
time = np.arange(len(signal)/sample_rate)
plt.plot(time, signal)
plt.plot(freqs[:N//2], amplitudes[:N//2])  # Само позитивни фреквенции
plt.xlabel("Фреквенција (Hz)")
plt.xlim(0,1900)
plt.ylabel("Амплитуда")
plt.title("Амплитуден спектар на Fletjta.wav")
plt.grid()
plt.show()

# Идентификација на тонови (ноти)
# Пример: најголемите амплитуди
peak_indices = np.argsort(amplitudes[:N//2])[-3:]  # Топ 3 фреквенции
peak_freqs = freqs[peak_indices]
print("Најдени фреквенции:", peak_freqs)

# Пребарување на нотите (пример за C4=261.63 Hz, D4=293.66 Hz, итн.)
notes = {
    261.63: "C4",
    293.66: "D4",
    329.63: "E4",
    349.23: "F4",
    392.00: "G4",
    440.00: "A4",
    493.88: "B4"
}

# Најблиска нота за секоја фреквенција
for freq in peak_freqs:
    closest_note = min(notes.keys(), key=lambda x: abs(x - freq))
    print(f"Фреквенција: {freq:.2f} Hz ~ Нота: {notes[closest_note]} ({closest_note} Hz)")