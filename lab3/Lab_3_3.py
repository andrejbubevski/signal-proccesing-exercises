import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftshift

N = 64
n = np.arange(N)

# Сигнали
x = np.tile([1, 0], N//2)  # [1,0,1,0,...]
y = np.cos(np.pi * n)      # cos(nπ) = (-1)^n
z = np.ones(N)             # Константа 1

# Проверка на врската x[n] = 0.5*(z[n] + y[n])
x_reconstructed = 0.5 * (z + y)

# ДФТ
X = fft(x)
Y = fft(y)
Z = fft(z)

# Проверка на врската X[k] = 0.5*(Z[k] + Y[k])
X_reconstructed = 0.5 * (Z + Y)

# Цртање
plt.figure(figsize=(12, 8))

# Временски домен
plt.subplot(2, 2, 1)
plt.stem(n, x, 'b', markerfmt='bo', basefmt=" ")
plt.title('x[n] = [1,0,1,0,...]')
plt.xlabel('n')
plt.grid()

plt.subplot(2, 2, 2)
plt.stem(n, y, 'g', markerfmt='go', basefmt=" ")
plt.title('y[n] = cos(nπ)')
plt.xlabel('n')
plt.grid()

plt.subplot(2, 2, 3)
plt.stem(n, z, 'r', markerfmt='ro', basefmt=" ")
plt.title('z[n] = 1')
plt.xlabel('n')
plt.grid()

plt.subplot(2, 2, 4)
plt.stem(n, x_reconstructed, 'm', markerfmt='mo', basefmt=" ")
plt.title('0.5*(z[n] + y[n])')
plt.xlabel('n')
plt.grid()

plt.tight_layout()
plt.show()

# ДФТ приказ
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.stem(n, np.abs(X), 'b', markerfmt='bo', basefmt=" ")
plt.title('Амплитуден спектар на X[k]')
plt.xlabel('k')
plt.grid()

plt.subplot(2, 2, 2)
plt.stem(n, np.abs(Y), 'g', markerfmt='go', basefmt=" ")
plt.title('Амплитуден спектар на Y[k]')
plt.xlabel('k')
plt.grid()

plt.subplot(2, 2, 3)
plt.stem(n, np.abs(Z), 'r', markerfmt='ro', basefmt=" ")
plt.title('Амплитуден спектар на Z[k]')
plt.xlabel('k')
plt.grid()

plt.subplot(2, 2, 4)
plt.stem(n, np.abs(X_reconstructed), 'm', markerfmt='mo', basefmt=" ")
plt.title('Амплитуден спектар на 0.5*(Z[k] + Y[k])')
plt.xlabel('k')
plt.grid()

plt.tight_layout()
plt.show()