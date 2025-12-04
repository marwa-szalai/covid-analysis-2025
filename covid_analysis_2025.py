import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('covid_2025_data.csv')
plt.plot(df['date'], df['new_cases'])
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.title('COVID-19 New Cases in 2025')
plt.show()
