import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft


def compare_signals(original, reconstructed, title):
    # Проверка во временски домен
    time_domain_diff = np.max(np.abs(original - reconstructed))
    print(f"{title} - Максимална разлика во временски домен: {time_domain_diff}")

    # Проверка во фреквенциски домен
    dft_original = fft(original)
    dft_reconstructed = fft(reconstructed)
    freq_domain_diff = np.max(np.abs(dft_original - dft_reconstructed))
    print(f"{title} - Максимална разлика во фреквенциски домен: {freq_domain_diff}")

    # Визуелизација
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.plot(original, 'b', label='Оригинален')
    plt.plot(reconstructed, 'r--', label='Реконструиран')
    plt.title(f'{title} - Временски домен')
    plt.legend()
    plt.grid()

    plt.subplot(1, 2, 2)
    plt.plot(np.abs(dft_original), 'b', label='Оригинален')
    plt.plot(np.abs(dft_reconstructed), 'r--', label='Реконструиран')
    plt.title(f'{title} - Амплитуден спектар')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()


# =================================================================
# 1. Споредба на сигналите x[n] и y[n] (делта функции)
# =================================================================
N = 64
n = np.arange(N)

x = np.zeros(N)
x[:8] = 1

y = np.zeros(N)
y[-8:] = 1

# Теоретски, y[n] = x[n-56]
y_reconstructed = np.roll(x, 56)

compare_signals(y, y_reconstructed, "Сигнали x[n] и y[n] (поместување)")

# =================================================================
# 2. Споредба на синусоидните сигнали
# =================================================================
x_sin = np.sin(np.pi * n / 16) + 2 * np.cos(np.pi * n / 8)
y_sin = np.sin(np.pi * n / 16 + np.pi / 3) + 2 * np.cos(np.pi * n / 8)

# Немаме аналитичка реконструкција, но можеме да провериме дека
# амплитудните спектри се исти
dft_x = fft(x_sin)
dft_y = fft(y_sin)

print("Разлика во амплитудни спектри:", np.max(np.abs(np.abs(dft_x) - np.abs(dft_y))))
print("Разлика во фазни спектри:", np.max(np.abs(np.angle(dft_x) - np.angle(dft_y))))

# =================================================================
# 3. Споредба на сигналите x[n], y[n], z[n]
# =================================================================
x_rect = np.tile([1, 0], N // 2)
y_cos = np.cos(np.pi * n)
z_ones = np.ones(N)

x_reconstructed = 0.5 * (z_ones + y_cos)

compare_signals(x_rect, x_reconstructed, "Сигнали x[n] и 0.5*(z[n]+y[n])")

# ДФТ споредба
dft_x = fft(x_rect)
dft_recon = 0.5 * (fft(z_ones) + fft(y_cos))

print("Разлика во ДФТ домен:", np.max(np.abs(dft_x - dft_recon)))