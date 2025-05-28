import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Вчитување на податоците
file_path = 'MKD-Kovid.xlsx'
data = pd.read_excel(file_path)

# Извлекување на датите и бројот на новозаразени
dates = pd.to_datetime(data.iloc[:, 0])
cases = data.iloc[:, 1].values

# Заменуваме NaN со 0, па потоа отстрануваме сите 0 вредности за визуелизација
cases = np.nan_to_num(cases, nan=0)
valid_indices = cases > 0
dates = dates[valid_indices]
cases = cases[valid_indices]

# Подвижна средна вредност
def moving_average(signal, M):
    return np.convolve(signal, np.ones(M)/M, mode='same')

# Медијански филтер
def median_filter(signal, M):
    result = []
    half_M = M // 2
    for i in range(len(signal)):
        window = signal[max(0, i - half_M): min(len(signal), i + half_M + 1)]
        result.append(np.median(window))
    return np.array(result)

# Должини на филтри
M_values = [3, 7]

# Цртање
plt.figure(figsize=(14, 8))
plt.plot(dates, cases, label='Оригинален сигнал (без 0)', color='gray', alpha=0.5)

for M in M_values:
    ma = moving_average(cases, M)
    med = median_filter(cases, M)
    plt.plot(dates, ma, label=f'Подвижна средна (M={M})')
    plt.plot(dates, med, linestyle='--', label=f'Медијана (M={M})')

plt.title('Филтриран сигнал на новозаразени со Ковид-19 во Македонија')
plt.xlabel('Датум')
plt.ylabel('Број на новозаразени')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(ticks=dates[::max(1, len(dates)//10)], labels=[date.strftime('%Y-%m-%d') for date in dates[::max(1, len(dates)//10)]], rotation=45)
plt.show()