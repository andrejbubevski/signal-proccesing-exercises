import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftshift

N = 64
n = np.arange(N)

# Сигнали
x = np.zeros(N)
x[:8] = 1  # x[n] = sum_{h=0}^7 δ[n-h]

y = np.zeros(N)
y[-8:] = 1  # y[n] = sum_{h=56}^63 δ[n-h]

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
plt.stem(n, x, 'b', markerfmt='bo', basefmt=" ")
plt.title('x[n]')
plt.xlabel('n')
plt.grid()

plt.subplot(2, 2, 2)
plt.stem(n, y, 'r', markerfmt='ro', basefmt=" ")
plt.title('y[n]')
plt.xlabel('n')
plt.grid()

# Амплитуден спектар
plt.subplot(2, 2, 3)
plt.stem(n, amp_X, 'b', markerfmt='bo', basefmt=" ")
plt.title('Амплитуден спектар на X[k]')
plt.xlabel('k')
plt.grid()

plt.subplot(2, 2, 4)
plt.stem(n, amp_Y, 'r', markerfmt='ro', basefmt=" ")
plt.title('Амплитуден спектар на Y[k]')
plt.xlabel('k')
plt.grid()

plt.tight_layout()
plt.show()

# Фазен спектар
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.stem(n, phase_X, 'b', markerfmt='bo', basefmt=" ")
plt.title('Фазен спектар на X[k]')
plt.xlabel('k')
plt.grid()

plt.subplot(1, 2, 2)
plt.stem(n, phase_Y, 'r', markerfmt='ro', basefmt=" ")
plt.title('Фазен спектар на Y[k]')
plt.xlabel('k')
plt.grid()

plt.tight_layout()
plt.show()