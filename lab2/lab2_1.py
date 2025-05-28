import numpy as np
from scipy.fft import fft
import cmath
import matplotlib.pyplot as plt

def dft_manual(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            angle = -2j * cmath.pi * k * n / N
            X[k] += x[n] * cmath.exp(angle)
    return X

# Тест сигнал
n = np.arange(8)
x = np.sin(2 * np.pi * n / 8)  # Чист синус со период 8

# Пресметка на DFT
X_manual = dft_manual(x)
X_scipy = fft(x)

# Поставување на графиконите
plt.figure(figsize=(14, 10))

# 1. Влезен сигнал (Временски домен)
plt.subplot(3, 2, 1)
plt.stem(x, linefmt='b-', markerfmt='bo', basefmt=' ')
plt.title("Влезен сигнал (Временски домен)")
plt.xlabel("n (индекс)")
plt.ylabel("Амплитуда")

# 2. Реален и Имагинарен дел (Рачно DFT)
plt.subplot(3, 2, 2)
plt.stem(np.real(X_manual), linefmt='b-', markerfmt='bo', basefmt=' ', label="Реален")
plt.stem(np.imag(X_manual), linefmt='r--', markerfmt='ro', basefmt=' ', label="Имагинарен")
plt.title("Рачно DFT: Реален и Имагинарен дел")
plt.xlabel("k (Фреквенција)")
plt.ylabel("Амплитуда")
plt.legend()

# 3. Амплитуден спектар (Рачно DFT)
plt.subplot(3, 2, 3)
plt.stem(np.abs(X_manual), linefmt='g-', markerfmt='go', basefmt=' ')
plt.title("Рачно DFT: Амплитуден спектар")
plt.xlabel("k (Фреквенција)")
plt.ylabel("|X[k]|")

# 4. Фазен спектар (Рачно DFT, Степенки)
plt.subplot(3, 2, 4)
plt.stem(np.angle(X_manual, deg=True), linefmt='m-', markerfmt='mo', basefmt=' ')
plt.title("Рачно DFT: Фазен спектар (°)")
plt.xlabel("k (Фреквенција)")
plt.ylabel("Фаза (°)")

# 5. Споредба на DFT: Рачно vs SciPy (Реален дел)
plt.subplot(3, 2, 5)
plt.stem(np.real(X_manual), linefmt='b-', markerfmt='bo', basefmt=' ', label="Рачно DFT")
plt.stem(np.real(X_scipy), linefmt='r--', markerfmt='rx', basefmt=' ', label="SciPy FFT")
plt.title("Споредба на DFT (Реален дел)")
plt.xlabel("k (Фреквенција)")
plt.ylabel("Амплитуда")
plt.legend()

# 6. Споредба на DFT: Рачно vs SciPy (Имагинарен дел)
plt.subplot(3, 2, 6)
plt.stem(np.imag(X_manual), linefmt='b-', markerfmt='bo', basefmt=' ', label="Рачно DFT")
plt.stem(np.imag(X_scipy), linefmt='r--', markerfmt='rx', basefmt=' ', label="SciPy FFT")
plt.title("Споредба на DFT (Имагинарен дел)")
plt.xlabel("k (Фреквенција)")
plt.ylabel("Амплитуда")
plt.legend()

plt.tight_layout()
plt.show()