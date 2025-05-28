import numpy as np
import matplotlib.pyplot as plt

# Параметри
T = np.linspace(0, 10, 1000)  # Аналогно време со 1000 точки
omega = 0.7 * np.pi
phi = 0.4

# Функција f(t) = sin(0.7 * pi * t + 0.4)
f_t = np.sin(omega * T + phi)

# Низата x[n] = sin(0.7 * pi * n + 0.4) за n = 0, 1, ..., 10
n = np.arange(0, 11)
x_n = np.sin(omega * n + phi)

# Примероци на растојание T_S = 0.125
T_S = 0.125
n_samples = np.arange(0, 10, T_S)
sampled_signal = np.sin(omega * n_samples + phi)

# Цртање на графикот
plt.figure(figsize=(10, 6))

# Прикажување на континуираниот сигнал
plt.plot(T, f_t, label=r'$f(t) = \sin(0.7 \pi t + 0.4)$', color='blue')

# Прикажување на низата со стапчиња
plt.stem(n, x_n, linefmt='r-', markerfmt='ro', basefmt='k', label=r'$x[n] = \sin(0.7 \pi n + 0.4)$')

# Прикажување на примероците на растојание T_S
plt.plot(n_samples, sampled_signal, 'go', label=r'$Samples\ at\ T_S = 0.125$')

# Означување на графикот
plt.title('Аналогни и дигитални сигнали')
plt.xlabel('Време (t или n)')
plt.ylabel('Амплитуда')
plt.legend()
plt.grid(True)

# Прикажи го графикот
plt.show()