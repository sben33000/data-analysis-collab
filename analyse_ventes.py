import pandas as pd

df = pd.read_csv("data/ventes.csv")
print(len(df))
print(df.head())
print(df.describe())
print(df.info())