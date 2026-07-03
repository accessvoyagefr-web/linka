import streamlit as st

# Configuration de la page
st.set_page_config(page_title="LINKA", page_icon="🔗", layout="wide")

# Style CSS pour le look futuriste
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }
    .big-font {
        font-size: 32px !important;
        color: #00f2ff;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Titre et Sous-titre
st.title("🔗 LINKA")
st.markdown('<p class="big-font">Votre portail d\'accès intelligent vers le web</p>', unsafe_allow_html=True)

# Zone de recherche
user_input = st.text_input("Quel site cherches-tu ?")

if user_input:
    st.write(f"Recherche en cours pour : {user_input}...")
    st.info("Je suis là uniquement pour vous aider à trouver des liens vers des sites web.")

# Section des Abonnements
st.header("Nos Plans d'abonnement")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Gratuit")
    st.write("• Recherche limitée")
    st.button("Choisir Gratuit")

with col2:
    st.subheader("Premium")
    st.write("• 9.99 € / mois")
    st.write("• Recherche illimitée")
    st.button("Choisir Premium")

with col3:
    st.subheader("Entreprise")
    st.write("• 19.99 € / mois")
    st.write("• Plusieurs comptes")
    st.button("Choisir Entreprise")
