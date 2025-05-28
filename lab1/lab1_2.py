import numpy as np
import matplotlib.pyplot as plt

# Parameters
n = np.arange(0, 11)
omega = 0.7 * np.pi
phi = 0.4

# Sequence x[n] = sin(0.7 * pi * n + 0.4)
x_n = np.sin(omega * n + phi)

# Plot discrete signal
plt.figure()
plt.stem(n, x_n, linefmt='r-', markerfmt='ro', basefmt='k', label=r'$x[n] = \sin(0.7 \pi n + 0.4)$')
plt.title('Discrete Signal')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Show plot
plt.show()