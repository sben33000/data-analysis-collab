import pandas as pd
print("pandas", pd.__version__)

ventes = pd.read_csv("data/ventes.csv")

print("dimensions :", ventes.shape)
ventes.info()

df_ventes = ventes
print(df_ventes.head())

#Nombre de valeurs manquantes
df_ventes.isna().sum()

#Remplacement des valeurs par "Inconnue"
df_ventes['ville'] = df_ventes['ville'].fillna('Inconnue')