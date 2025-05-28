import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


# Вчитување на оргулите
sample_rate_org, org_signal = wavfile.read('Orgulji.wav')
org_signal = org_signal[:, 0]  # Лев канал

# Основна информација
print(f"Фреквенција на семплирање: {sample_rate_org} Hz")
print(f"Број на примероци: {len(org_signal)}")
print(f"Времетраење: {len(org_signal) / sample_rate_org:.2f} секунди")


# Пресметка на DFT
def compute_dft(signal, sr):
    N = len(signal)
    dft = np.fft.fft(signal)
    freqs = np.fft.fftfreq(N, 1 / sr)
    amps = np.abs(dft) / N
    return freqs[:N // 2], amps[:N // 2]


freqs_org, amps_org = compute_dft(org_signal, sample_rate_org)

# Приказ на спектарот
plt.figure(figsize=(12, 6))
plt.plot(freqs_org, amps_org, color='purple')
plt.title("Амплитуден спектар на Orgulji.wav")
plt.xlabel("Фреквенција (Hz)")
plt.xlim(0, 1900)
plt.ylabel("Амплитуда")
plt.grid()
plt.show()

# Идентификација на тонови
notes = {
    261.63: "C4", 293.66: "D4", 329.63: "E4",
    349.23: "F4", 392.00: "G4", 440.00: "A4",
    493.88: "B4", 523.25: "C5"
}


def find_notes(freqs, amps, top=3):
    peaks = np.argsort(amps)[-top:]
    return freqs[peaks]


org_peaks = find_notes(freqs_org, amps_org)
print("\nДоминантни фреквенции:")
for freq in org_peaks:
    note = min(notes.keys(), key=lambda x: abs(x - freq))
    print(f"{freq:.2f} Hz ~ {notes[note]} ({note} Hz)")

# Споредба со флејта (ако е вчитана)
try:
    _, fl_signal = wavfile.read('Flejta.wav')
    fl_signal = fl_signal[:, 0]
    freqs_fl, amps_fl = compute_dft(fl_signal, sample_rate_org)

    plt.figure(figsize=(12, 6))
    plt.plot(freqs_fl, amps_fl, label='Флејта', alpha=0.7)
    plt.plot(freqs_org, amps_org, label='Оргуљи', alpha=0.7)
    plt.title("Споредба на спектри")
    plt.xlabel("Фреквенција (Hz)")
    plt.xlim(0,2500)
    plt.ylabel("Амплитуда")
    plt.legend()
    plt.grid()
    plt.show()

except FileNotFoundError:
    print("\nНема пронајдено Fletjta.wav за споредба")