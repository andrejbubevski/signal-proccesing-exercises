import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft
from scipy.io import wavfile
import librosa   # библиотека за читање mp3
import sounddevice as sd

from scipy import signal

samplerate, data = wavfile.read('carmenscene.wav') # со ова се чита звук снимен во WAV облик
print(' стапка на земање примероци (фреквенција) ', samplerate, 'Херци')

N = len(data)
print(' должина на звучниот сигнал ', N)

n = np.asarray(list(range(0,N)))   # реден број на примерокот (дигитално време)
frek = np.linspace(0,samplerate, N) # N фреквенции до најголемата фреквенција
plt.figure()
plt.plot(n, data)
plt.title('Изглед на сигналот')
plt.show()

Fur = fft(data)
#  целиот спектар

#print(data[:10])
#print(Fur[:10])

#plt.figure()
plt.plot(frek, abs(Fur))
plt.title('Спектар на целиот сигнал')
plt.xlim([0, samplerate / 2])
plt.xlabel(' фреквенција ')
plt.show()

plt.plot(frek, abs(Fur))
plt.title('Нискофреквентен дел од спектарот на сигналот')
plt.xlim([0, samplerate / 5])
plt.xlabel(' фреквенција ')
plt.show()

# Дел во кој прво се филтрира па се земаат примероци
Skokanje = 5
sos = signal.butter(20, 0.2, 'low', output='sos', analog = False)  # ред 10, фреквенција 3000 Херци
filtered = signal.sosfilt(sos, data)

Fur = fft(filtered)
nFur = np.asarray(list(range(0,N)))
plt.plot(frek, abs(Fur))
plt.title('Спектар на филтрираниот сигнал')
plt.xlim([0, samplerate / 5])
plt.xlabel(' фреквенција ')
plt.show()


#Skokanje = 5  # колку примероци да се прескокнат, односно колку пати се намалува стапката на земање примероци

Filtrirana = filtered[0::Skokanje]
NewSampleRate = samplerate // Skokanje

sd.play(Filtrirana, NewSampleRate)

