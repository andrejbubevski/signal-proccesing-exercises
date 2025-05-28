import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import ellip, lfilter

# Генерирање на сигнал x[n] = sin(nπ/12) + sin(7nπ/12)
n = np.arange(128)
x = np.sin(n * np.pi / 12) + np.sin(7 * n * np.pi / 12)

# Параметри за филтерот
rp = 5       # бранување во пропусен опсег (dB)
rs = 50      # слабеење во непропусен опсег (dB)
Wn = 0.4     # гранична фреквенција (0 < Wn < 1)
N = 10       # ред на филтерот

# Нискофреквентен елиптичен филтер
b_low, a_low = ellip(N, rp, rs, Wn, btype='low', analog=False)
y_low = lfilter(b_low, a_low, x)

# Високофреквентен елиптичен филтер
b_high, a_high = ellip(N, rp, rs, Wn, btype='high', analog=False)
y_high = lfilter(b_high, a_high, x)

# Функција за приказ на сигнал и спектар
def plot_signal_and_spectrum(signal, title):
    plt.figure(figsize=(10, 4))

    # Временски домен
    plt.subplot(1, 2, 1)
    plt.plot(signal)
    plt.title(f'{title} - Сигнал')
    plt.xlabel('n')
    plt.ylabel('Амплитуда')
    plt.grid(True)

    # Фреквентен домен
    plt.subplot(1, 2, 2)
    spectrum = np.abs(np.fft.fft(signal))
    freqs = np.fft.fftfreq(len(signal), d=1)
    plt.plot(freqs[:len(freqs)//2], spectrum[:len(spectrum)//2])
    plt.title(f'{title} - Спектар')
    plt.xlabel('Фреквенција')
    plt.ylabel('|X[k]|')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Приказ
plot_signal_and_spectrum(x, "Оригинален сигнал")
plot_signal_and_spectrum(y_low, "Исфилтриран - Нискофреквентен")
plot_signal_and_spectrum(y_high, "Исфилтриран - Високофреквентен")