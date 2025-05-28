import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


# Function to analyze a single audio file
def analyze_audio(filename, color, label):
    try:
        sample_rate, signal = wavfile.read(filename)
        signal = signal[:, 0]  # Take left channel
        N = len(signal)
        duration = N / sample_rate

        # Time domain
        time = np.linspace(0, duration, N)

        # Frequency domain
        dft = np.fft.fft(signal)
        freqs = np.fft.fftfreq(N, 1 / sample_rate)
        amplitudes = np.abs(dft) / N  # Normalized amplitudes

        return {
            'time': time,
            'signal': signal,
            'freqs': freqs[:N // 2],
            'amplitudes': amplitudes[:N // 2],
            'color': color,
            'label': label,
            'peaks': None
        }
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return None


# Analyze both files
flute = analyze_audio('Flejta.wav', 'blue', 'Flute')
organs = analyze_audio('Orgulji.wav', 'red', 'Organ')

if flute and organs:
    # 1. Plot time domain signals together
    plt.figure(figsize=(14, 5))
    plt.plot(flute['time'], flute['signal'], color=flute['color'],
             alpha=0.7, label=flute['label'])
    plt.plot(organs['time'], organs['signal'], color=organs['color'],
             alpha=0.7, label=organs['label'])
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.title("Time Domain Comparison")
    plt.legend()
    plt.grid()
    plt.show()

    # 2. Plot frequency domain together
    plt.figure(figsize=(14, 5))
    plt.plot(flute['freqs'], flute['amplitudes'], color=flute['color'],
             alpha=0.7, label=flute['label'])
    plt.plot(organs['freqs'], organs['amplitudes'], color=organs['color'],
             alpha=0.7, label=organs['label'])
    plt.xlabel("Frequency (Hz)")
    plt.xlim(0, 2000)  # Focus on 0-2kHz range
    plt.ylabel("Amplitude")
    plt.title("Frequency Spectrum Comparison")
    plt.legend()
    plt.grid()
    plt.show()


    # 3. Find and compare peaks
    def find_peaks(analysis, top_n=3):
        peaks = np.argsort(analysis['amplitudes'])[-top_n:]
        return analysis['freqs'][peaks]


    flute['peaks'] = find_peaks(flute)
    organs['peaks'] = find_peaks(organs)

    # Note dictionary
    notes = {
        261.63: "C4", 293.66: "D4", 329.63: "E4",
        349.23: "F4", 392.00: "G4", 440.00: "A4",
        493.88: "B4", 523.25: "C5"
    }


    def find_closest_note(freq):
        closest = min(notes.keys(), key=lambda x: abs(x - freq))
        return notes[closest], closest


    print("\nDominant Frequencies Comparison:")
    print(f"{'Frequency (Hz)':<15} {'Flute Note':<15} {'Organ Note':<15}")

    for i in range(3):
        fl_freq = flute['peaks'][i]
        org_freq = organs['peaks'][i]

        fl_note, fl_note_freq = find_closest_note(fl_freq)
        org_note, org_note_freq = find_closest_note(org_freq)

        print(
            f"{fl_freq:<15.2f} {fl_note + ' (' + str(fl_note_freq) + 'Hz)':<15} {org_note + ' (' + str(org_note_freq) + 'Hz)':<15}")

    # 4. Plot harmonic content comparison
    plt.figure(figsize=(14, 5))

    # Normalize amplitudes for better comparison
    flute_norm = flute['amplitudes'] / np.max(flute['amplitudes'])
    organs_norm = organs['amplitudes'] / np.max(organs['amplitudes'])

    plt.plot(flute['freqs'], flute_norm, color=flute['color'],
             label=flute['label'] + ' (normalized)')
    plt.plot(organs['freqs'], organs_norm, color=organs['color'],
             label=organs['label'] + ' (normalized)')

    plt.xlabel("Frequency (Hz)")
    plt.xlim(0, 4000)  # Extended to show harmonics
    plt.ylabel("Normalized Amplitude")
    plt.title("Normalized Spectrum Comparison (Showing Harmonics)")
    plt.legend()
    plt.grid()
    plt.show()