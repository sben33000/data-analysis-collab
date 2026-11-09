import pandas as pd

df = pd.read_csv("data/ventes.csv")

df["chiffre_affaires"] = df["quantite"] * df["prix_unitaire"]
print("CA total :", round(df["chiffre_affaires"].sum(), 2), "€")

ca_categorie = df.groupby("categorie")["chiffre_affaires"].sum().sort_values(ascending=False)
print(ca_categorie)