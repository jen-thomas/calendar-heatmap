import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/regla_test.csv')
df['date'] = pd.to_datetime(df.date, yearfirst=True)

# create day and month columns
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

data = df.pivot("month", "day", "bleeding.value")

sns.heatmap(data)
plt.show()