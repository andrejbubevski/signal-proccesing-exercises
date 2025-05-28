import numpy as np
from scipy.io import wavfile

def print_signal_info(filename, max_samples=10):
    try:
        # Read WAV file
        sample_rate, signal = wavfile.read(filename)

        print(f"\n=== {filename} ===")
        print(f"Sample rate: {sample_rate} Hz")
        print(f"Total samples: {len(signal)}")
        print(f"Duration: {len(signal) / sample_rate:.2f} seconds")

        # Print channel info
        if len(signal.shape) == 1:
            print("Mono audio (1 channel)")
            print("\nFirst 10 samples:")
            print(signal[:max_samples])
        else:
            print(f"Stereo audio ({signal.shape[1]} channels)")
            print("\nFirst 10 samples - Left channel:")
            print(signal[:max_samples, 0])
            print("\nFirst 10 samples - Right channel:")
            print(signal[:max_samples, 1])

        return signal

    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return None


# Print signals for both files
flute_signal = print_signal_info('Flejta.wav')
organs_signal = print_signal_info('Orgulji.wav')

# If you want to see more samples, change max_samples
# Example: print_signal_info('Fletjta.wav', max_samples=20)