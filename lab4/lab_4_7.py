import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load the signal
sample_rate, signal = wavfile.read('Orgulji.wav')
signal = signal[:, 0]  # Left channel only
N = len(signal)
duration = N / sample_rate

# Basic information
print(f"Sampling frequency: {sample_rate} Hz")
print(f"Number of samples: {N}")
print(f"Duration: {duration:.2f} seconds")

# Create time array for plotting
time = np.linspace(0, duration, N)

# Plot the time-domain signal
plt.figure(figsize=(12, 4))
plt.plot(time, signal)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Time Domain Signal")
plt.grid()
plt.show()

# Calculate DFT
dft = np.fft.fft(signal)
freqs = np.fft.fftfreq(N, 1/sample_rate)
amplitudes = np.abs(dft) / N  # Normalization

# Plot the amplitude spectrum
plt.figure(figsize=(12, 4))
plt.plot(freqs[:N//2], amplitudes[:N//2])  # Only positive frequencies
plt.xlabel("Frequency (Hz)")
plt.xlim(0, 1900)
plt.ylabel("Amplitude")
plt.title("Amplitude Spectrum")
plt.grid()
plt.show()

# Identify tones (notes)
peak_indices = np.argsort(amplitudes[:N//2])[-3:]  # Top 3 frequencies
peak_freqs = freqs[peak_indices]
print("Found frequencies:", peak_freqs)

# Note dictionary
notes = {
    261.63: "C4",
    293.66: "D4",
    329.63: "E4",
    349.23: "F4",
    392.00: "G4",
    440.00: "A4",
    493.88: "B4"
}

# Find closest note for each frequency
for freq in peak_freqs:
    closest_note = min(notes.keys(), key=lambda x: abs(x - freq))
    print(f"Frequency: {freq:.2f} Hz ~ Note: {notes[closest_note]} ({closest_note} Hz)")