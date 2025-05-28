import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft
from scipy.io import wavfile
import sounddevice as sd

from scipy import signal

samplerate, data = wavfile.read('carmenscene.wav') # со ова се чита звук снимен во WAV облик
print(' стапка на земање примероци (фреквенција) ', samplerate, 'Херци')

N = len(data)
print(' должина на звучниот сигнал ', N)
#print(data[100000:100100])

n = np.asarray(list(range(0,N)))   # реден број на примерокот (дигитално време)
frek = np.linspace(0,samplerate, N) # N фреквенции до најголемата фреквенција
plt.figure()
plt.plot(n, data)
plt.title('Изглед на сигналот')
plt.show()

Fur = fft(data)
#  целиот спектар

#plt.figure()
plt.plot(frek, abs(Fur))
plt.title('Спектар на целиот сигнал')
plt.xlim([0, samplerate / 2])
plt.xlabel(' фреквенција ')
plt.show()

plt.plot(frek, abs(Fur))
plt.title('Нискофреквентен дел од спектарот на сигналот')
plt.xlim([0, samplerate / 4])
plt.xlabel(' фреквенција ')
plt.show()

# Дел во кој само се земаат примероци без да се филтрира
Skokanje = 5  # колку примероци да се прескокнат, односно колку пати се намалува стапката на земање примероци

Proretchena = data[0::Skokanje]
NewSampleRate = samplerate // Skokanje

sd.play(Proretchena, NewSampleRate)
