aimport streamlit as st
import pandas as pd

# Configurer la page
st.set_page_config(page_title="Veille VSS Culture", layout="wide")
st.title("📚 Veille – Violences sexuelles et sexistes dans la culture")

# Lire le CSV local
df = pd.read_csv("veille.csv", encoding='utf-8')  # veille.csv doit être à la racine du dépôt

# Convertir la colonne date avec le format exact et trier
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y %H:%M:%S", errors='coerce')
df = df.sort_values(by="date", ascending=False)

# Filtre par mot-clé (si tu ajoutes une colonne Mots-cles plus tard)
if "Mots-cles" in df.columns:
    mot_cle = st.selectbox(
        "Filtrer par mot-clé",
        ["Tous"] + sorted({k for tags in df["Mots-cles"].dropna() for k in tags.split(", ")})
    )
    if mot_cle != "Tous":
        df = df[df["Mots-cles"].str.contains(mot_cle, na=False)]

# Affichage des articles
for _, row in df.iterrows():
    st.markdown(f"### {row['Titre']}")
    st.write(f"🗞️ {row['source']} — 🗓️ {row['date'].strftime('%d/%m/%Y %H:%M')}")
    st.markdown(f"[Lire l'article]({row['lien']})")
    if "Mots-cles" in df.columns:
        st.write(f"🏷️ {row.get('Mots-cles','')}")
    st.markdown("---")

