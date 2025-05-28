import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

# Читање на податоците
KadeSePodatocite = './'  # Доколку е во ист фолдер со проектот
Podatoci = pd.read_excel(KadeSePodatocite + 'SandP500.xlsx')

# Читање на датум и вредности
dates = pd.to_datetime(Podatoci.iloc[:, 0])  # Осигуруваме дека се datetime
SP500 = Podatoci.iloc[:, 1].values

# Информации
print(Podatoci.info())
print(Podatoci.head())
print(Podatoci.tail())

# Функција за тежински подвижен просек
def weighted_moving_average(signal, M):
    weights = np.arange(M, 0, -1)
    filtered = []

    for i in range(len(signal)):
        if i < M:
            segment = signal[:i + 1]
            w = weights[-(i + 1):]
        else:
            segment = signal[i - M + 1:i + 1]
            w = weights
        avg = np.dot(segment, w) / np.sum(w)
        filtered.append(avg)

    return np.array(filtered)

# Должини на филтер
M_values = [3, 7, 10]

# Исцртување
plt.figure(figsize=(14, 8))
plt.plot(dates, SP500, label='Оригинален сигнал', color='gray', linewidth=1)

for M in M_values:
    filtered = weighted_moving_average(SP500, M)
    plt.plot(dates, filtered, label=f'Филтриран сигнал (M={M})')

plt.title('Филтрирање на S&P 500 со тежински просек')
plt.xlabel('Датум')
plt.ylabel('Вредност на индексот')
plt.legend()
plt.grid(True)

# Форматирање на датумите
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gcf().autofmt_xdate()

plt.tight_layout()
plt.show()
