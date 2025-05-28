import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = np.linspace(0, 10, 1000)
omega = 0.7 * np.pi
phi = 0.4

# Function f(t) = sin(0.7 * pi * t + 0.4)
f_t = np.sin(omega * T + phi)

# Plot continuous signal
plt.figure()
plt.plot(T, f_t, label=r'$f(t) = \sin(0.7 \pi t + 0.4)$', color='blue')
plt.title('Continuous Signal')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Show plot
plt.show()