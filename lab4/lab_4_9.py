import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


def analyze_audio(filename, color, label, threshold=0.05):
    try:
        sample_rate, signal = wavfile.read(filename)
        signal = signal[:, 0] if len(signal.shape) > 1 else signal
        signal = signal / np.max(np.abs(signal))  # Normalize

        # Find non-silent portions
        abs_signal = np.abs(signal)
        threshold = threshold * np.max(abs_signal)
        active_samples = np.where(abs_signal > threshold)[0]

        if len(active_samples) == 0:
            print(f"No active signal found in {filename}")
            return None

        start_idx = active_samples[0]
        end_idx = active_samples[-1]
        active_signal = signal[start_idx:end_idx + 1]

        # Time domain
        active_time = np.arange(len(active_signal)) / sample_rate

        # Frequency domain (only active portion)
        N = len(active_signal)
        dft = np.fft.fft(active_signal)
        freqs = np.fft.fftfreq(N, 1 / sample_rate)
        amplitudes = np.abs(dft) / N

        return {
            'time': active_time,
            'signal': active_signal,
            'freqs': freqs[:N // 2],
            'amplitudes': amplitudes[:N // 2],
            'color': color,
            'label': label,
            'start_idx': start_idx,
            'end_idx': end_idx
        }

    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return None


# Usage example:
flute = analyze_audio('Flejta.wav', 'green', 'Flute')
organs = analyze_audio('Orgulji.wav', 'red', 'Organ')

if flute and organs:
    # Plot active signal portions
    plt.figure(figsize=(14, 5))
    plt.plot(flute['time'], flute['signal'], color=flute['color'], label=flute['label'])
    plt.plot(organs['time'], organs['signal'], color=organs['color'], label=organs['label'])
    plt.title("Active Signal Portions")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()
    plt.show()

    # Plot DFT of active portions
    plt.figure(figsize=(14, 5))
    plt.plot(flute['freqs'], flute['amplitudes'], color=flute['color'], label=flute['label'])
    plt.plot(organs['freqs'], organs['amplitudes'], color=organs['color'], label=organs['label'])
    plt.title("DFT of Active Signal Portions")
    plt.xlabel("Frequency (Hz)")
    plt.xlim(0, 2000)
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()
    plt.show()