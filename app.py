import streamlit as st
import pandas as pd

st.set_page_config(page_title="Veille VSS Culture", layout="wide")
st.title("📚 Veille – Violences sexuelles et sexistes dans la culture")

# Lien CSV public de ton Google Sheets
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1v…/pub?output=csv"
"

# Charger les données
df = pd.read_csv(CSV_URL)

# Convertir la date
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
df = df.sort_values(by="Date", ascending=False)

# Filtre par mot-clé
mot_cle = st.selectbox("Filtrer par mot-clé", ["Tous"] + sorted({k for tags in df["Mots-cles"].dropna() for k in tags.split(", ")}))
if mot_cle != "Tous":
    df = df[df["Mots-cles"].str.contains(mot_cle, na=False)]

# Affichage
for _, row in df.iterrows():
    st.markdown(f"### {row['Titre']}")
    st.write(f"🗞️ {row['Source']} — 🗓️ {row['Date'].strftime('%d/%m/%Y')}")
    st.markdown(f"[Lire l'article]({row['Lien']})")
    if "Mots-cles" in row:
        st.write(f"🏷️ {row['Mots-cles']}")
    st.markdown("---")
