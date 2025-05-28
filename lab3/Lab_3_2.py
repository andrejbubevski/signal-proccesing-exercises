import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftshift

N = 64
n = np.arange(N)

# Сигнали
x = np.sin(np.pi * n / 16) + 2 * np.cos(np.pi * n / 8)
y = np.sin(np.pi * n / 16 + np.pi/3) + 2 * np.cos(np.pi * n / 8)

# ДФТ
X = fft(x)
Y = fft(y)

# Амплитуда и фаза
amp_X = np.abs(X)
phase_X = np.angle(X)

amp_Y = np.abs(Y)
phase_Y = np.angle(Y)

# Цртање
plt.figure(figsize=(12, 8))

# Временски домен
plt.subplot(2, 2, 1)
plt.plot(n, x, 'b')
plt.title('x[n] = sin(πn/16) + 2cos(πn/8)')
plt.xlabel('n')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(n, y, 'r')
plt.title('y[n] = sin(πn/16 + π/3) + 2cos(πn/8)')
plt.xlabel('n')
plt.grid()

# Амплитуден спектар
plt.subplot(2, 2, 3)
plt.stem(n[:N//2], amp_X[:N//2], 'b', markerfmt='bo', basefmt=" ")
plt.title('Амплитуден спектар на X[k] (први 32 бита)')
plt.xlabel('k')
plt.grid()

plt.subplot(2, 2, 4)
plt.stem(n[:N//2], amp_Y[:N//2], 'r', markerfmt='ro', basefmt=" ")
plt.title('Амплитуден спектар на Y[k] (први 32 бита)')
plt.xlabel('k')
plt.grid()

plt.tight_layout()
plt.show()

# Фазен спектар (прикажани само релевантни бинови)
k_show = [2, 4, N-4, N-2]  # Бинари каде има енергија

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.stem(k_show, phase_X[k_show], 'b', markerfmt='bo', basefmt=" ")
plt.title('Фазен спектар на X[k] (клучни бинови)')
plt.xlabel('k')
plt.grid()

plt.subplot(1, 2, 2)
plt.stem(k_show, phase_Y[k_show], 'r', markerfmt='ro', basefmt=" ")
plt.title('Фазен спектар на Y[k] (клучни бинови)')
plt.xlabel('k')
plt.grid()

plt.tight_layout()
plt.show()