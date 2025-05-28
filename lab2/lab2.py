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


# Пример на употреба
if __name__ == "__main__":
    x = np.array([13, 2, 3, 10])  # Тест низа

    # DFT пресметка
    X_manual = dft_manual(x)
    X_scipy = fft(x)

    # Визуелизација
    plt.figure(figsize=(12, 10))

    # 1. Влезна низа (временски домен)
    plt.subplot(2, 2, 1)
    plt.stem(x, linefmt='b-', markerfmt='bo', basefmt=' ')  # Без use_line_collection
    plt.title("Влезна низа (временски домен)")
    plt.xlabel("n (индекс)")
    plt.ylabel("Амплитуда")

    # 2. Реален и имагинарен дел на DFT
    plt.subplot(2, 2, 2)
    plt.stem(np.real(X_manual), linefmt='b-', markerfmt='bo', basefmt=' ', label="Реален дел")
    plt.stem(np.imag(X_manual), linefmt='r--', markerfmt='ro', basefmt=' ', label="Имагинарен дел")
    plt.title("Реален и имагинарен дел на DFT")
    plt.xlabel("k (честота)")
    plt.ylabel("Амплитуда")
    plt.legend()

    # 3. Амплитуден спектар
    plt.subplot(2, 2, 3)
    plt.stem(np.abs(X_manual), linefmt='g-', markerfmt='go', basefmt=' ')
    plt.title("Амплитуден спектар")
    plt.xlabel("k (честота)")
    plt.ylabel("|X[k]|")

    # 4. Фазен спектар (во степени)
    plt.subplot(2, 2, 4)
    plt.stem(np.angle(X_manual, deg=True), linefmt='m-', markerfmt='mo', basefmt=' ')
    plt.title("Фазен спектар (во степени)")
    plt.xlabel("k (честота)")
    plt.ylabel("Фаза (°)")

    plt.tight_layout()
    plt.show()