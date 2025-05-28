import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def plot_filled_waveform(filename, max_samples=1000):
    try:
        # Read WAV file
        sample_rate, signal = wavfile.read(filename)

        # Prepare time axis
        duration = len(signal) / sample_rate
        time = np.linspace(0, duration, len(signal))

        # Create figure
        plt.figure(figsize=(14, 5))

        if len(signal.shape) == 1:  # Mono
            plt.fill_between(time[:max_samples], signal[:max_samples],
                             color='blue', alpha=0.5, label='Mono Signal')
            plt.plot(time[:max_samples], signal[:max_samples],
                     color='blue', alpha=0.8, linewidth=0.5)
        else:  # Stereo
            # Left channel
            plt.fill_between(time[:max_samples], signal[:max_samples, 0],
                             color='blue', alpha=0.3, label='Left Channel')
            plt.plot(time[:max_samples], signal[:max_samples, 0],
                     color='blue', alpha=0.7, linewidth=0.5)

            # Right channel
            plt.fill_between(time[:max_samples], signal[:max_samples, 1],
                             color='red', alpha=0.3, label='Right Channel')
            plt.plot(time[:max_samples], signal[:max_samples, 1],
                     color='red', alpha=0.7, linewidth=0.5)

        plt.title(f'Waveform: {filename}', fontsize=14)
        plt.xlabel('Time (seconds)', fontsize=12)
        plt.ylabel('Amplitude', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.legend(fontsize=10)
        plt.show()

    except FileNotFoundError:
        print(f"Error: {filename} not found!")


# Plot both signals with filled waveforms
print("Plotting Flejta.wav...")
plot_filled_waveform('Flejta.wav')

print("\nPlotting Orgulji.wav...")
plot_filled_waveform('Orgulji.wav')