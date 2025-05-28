import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, lfilter

# Читање на аудио фајл
fs, data = wavfile.read('carmenscene.wav')

# Ако аудио сигналот е стерео, земи само еден канал
if len(data.shape) > 1:
    data = data[:, 0]

# Функција за нископропусен филтер
def lowpass_filter(data, cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low')
    y = lfilter(b, a, data)
    return y

# Функција за земање секој n-ти примерок
def downsample(data, step):
    return data[::step]

# Пробај различни фактори
for n in [2, 3, 4, 5]:
    # Без филтрирање
    downsampled_raw = downsample(data, n)
    wavfile.write(f'downsampled_raw_{n}.wav', fs // n, downsampled_raw.astype(np.int16))

    # Со филтрирање
    filtered = lowpass_filter(data, cutoff=fs//(2*n), fs=fs)
    downsampled_filtered = downsample(filtered, n)
    wavfile.write(f'downsampled_filtered_{n}.wav', fs // n, downsampled_filtered.astype(np.int16))