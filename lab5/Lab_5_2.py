import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the data from the provided file
file_path = "SandP500.xlsx"
data = pd.read_excel(file_path)

# Extract dates and values
dates = data.iloc[:, 0]
sp500 = data.iloc[:, 1]

# Plot the original S&P 500 data
plt.figure(figsize=(14, 6))
plt.plot(dates, sp500, label='S&P 500', color='green')
plt.title('Оригинален сигнал - S&P 500')
plt.xlabel('Датум')
plt.ylabel('Индекс вредност')
plt.legend()
plt.grid(True)

# Format x-axis to show only date
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gcf().autofmt_xdate()

plt.tight_layout()
plt.show()
