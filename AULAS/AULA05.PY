import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./dados/dados.csv')

print(df.head())

plt.boxplot(df['nota'])
plt.title