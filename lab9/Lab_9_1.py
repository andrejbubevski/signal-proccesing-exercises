import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.io import wavfile
import sounddevice as sd
import os

# Функција за пресметка на SNR
def calculate_snr(original, quantized):
    noise = original - quantized
    signal_power = np.mean(original**2)
    noise_power = np.mean(noise**2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

# Креира директориум за аудио излез
output_dir = 'kvantizirani_audio'
os.makedirs(output_dir, exist_ok=True)

# Читање WAV
samplerate, dataOrig = wavfile.read('zajdi.wav')
print('Стапка на земање примероци:', samplerate, 'Hz')

# Ако е стерео -> земи втор канал
if len(dataOrig.shape) > 1:
    data = dataOrig[: len(dataOrig) // 15, 1]
else:
    data = dataOrig[: len(dataOrig) // 15]

# Нормализација
Najgolema = max(abs(data))
data = data / Najgolema
N = len(data)

n = np.arange(N)
frek = np.linspace(0, samplerate, N)

# Оригинален спектар
Fur = fft(data)
plt.figure()
plt.plot(frek, abs(Fur))
plt.title('Фреквенциски спектар на оригиналниот сигнал')
plt.xlim([0, samplerate / 2])
plt.ylim([0, 500])
plt.xlabel('Фреквенција [Hz]')
plt.grid()
plt.show()

# Квантизација со различен број бита
biti_lista = [2, 4, 6, 8, 12, 16]
for BrojNaBiti in biti_lista:
    print(f'\n➡️ Квантизација со {BrojNaBiti} бита')

    max_val = (2 ** (BrojNaBiti - 1)) - 1
    dataCeli = np.round(data * max_val).astype(int)
    kvantiziran = dataCeli / max_val

    # Спектар
    FurKvant = fft(kvantiziran)
    plt.figure()
    plt.plot(frek, abs(FurKvant))
    plt.title(f'Спектар со {BrojNaBiti} бита')
    plt.xlim([0, samplerate / 2])
    plt.ylim([0, 500])
    plt.xlabel('Фреквенција [Hz]')
    plt.grid()
    plt.show()

    # SNR пресметка
    snr = calculate_snr(data, kvantiziran)
    print(f'SNR за {BrojNaBiti} бита: {snr:.2f} dB')

    # Снимање аудио
    filename = f'{output_dir}/carmen_{BrojNaBiti}bit.wav'
    kvantiziran_int16 = (kvantiziran * 32767).astype(np.int16)
    wavfile.write(filename, samplerate, kvantiziran_int16)
    print(f'Аудио зачувано: {filename}')

    # Опционално: слушање
    #sd.play(kvantiziran, samplerate)
    #sd.wait()