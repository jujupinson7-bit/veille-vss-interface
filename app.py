import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Veille VSS Culture", layout="wide")
st.title("📚 Veille – Violences sexuelles et sexistes dans la culture")

# Lire le CSV local
# Assure-toi que le fichier 'veille.csv' est dans le même dépôt que app.py
df = pd.read_csv("veille.csv", encoding='utf-8')

# Nettoyer les caractères accentués ou illisibles
df = df.applymap(lambda x: x.encode('utf-8', errors='ignore').decode('utf-8') if isinstance(x, str) else x)

# Convertir la colonne Date en datetime et trier
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
df = df.sort_values(by="Date", ascending=False)

# Filtre par mot-clé
mot_cle = st.selectbox(
    "Filtrer par mot-clé",
    ["Tous"] + sorted({k for tags in df["Mots-cles"].dropna() for k in tags.split(", ")})
)
if mot_cle != "Tous":
    df = df[df["Mots-cles"].str.contains(mot_cle, na=False)]

# Affichage des articles
for _, row in df.iterrows():
    st.markdown(f"### {row['Titre']}")
    st.write(f"🗞️ {row['Source']} — 🗓️ {row['Date'].strftime('%d/%m/%Y')}")
    st.markdown(f"[Lire l'article]({row['Lien']})")
    if "Mots-cles" in row:
        st.write(f"🏷️ {row['Mots-cles']}")
    st.markdown("---")

