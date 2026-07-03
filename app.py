import streamlit as st

# Configuration de la page
st.set_page_config(page_title="LINKA", page_icon="🔗", layout="wide")

# Style CSS
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); color: white; }
    .big-font { font-size: 32px !important; color: #00f2ff; font-weight: bold; text-align: center; }
    .price-card { background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 15px; text-align: center; border: 1px solid #00f2ff; height: 100%; }
    .price-tag { font-size: 24px; font-weight: bold; color: #00f2ff; }
    .header-btns { text-align: right; }
    </style>
    """, unsafe_allow_html=True)

# Barre supérieure : Langue et Connexion
col_main, col_lang, col_login = st.columns([6, 1, 1])
with col_lang:
    st.selectbox("Langue", ["FR", "EN", "ES"], label_visibility="collapsed")
with col_login:
    st.button("Connexion 👤")

# Titre
st.markdown('<p class="big-font">🔗 LINKA - Votre portail d\'accès intelligent</p>', unsafe_allow_html=True)

# Zone de recherche
user_input = st.text_input("Quel site cherches-tu ?")

# Section des Abonnements
st.write("<br><br>", unsafe_allow_html=True)
st.header("Nos Plans d'abonnement")

col1, col2, col3 = st.columns(3)

def create_card(title, price, features):
    st.markdown(f"""
    <div class="price-card">
        <h3>{title}</h3>
        <p class="price-tag">{price}</p>
        <hr>
        <p>{features}</p>
    </div>
    """, unsafe_allow_html=True)

with col1:
    create_card("Gratuit", "0 €", "• 5 recherches/jour<br>• Accès standard")
    st.button("Choisir Gratuit", key="btn1")
with col2:
    create_card("Premium", "9.99 €", "• Illimité<br>• Support prioritaire")
    st.button("Choisir Premium", key="btn2")
with col3:
    create_card("Entreprise", "19.99 €", "• Utilisateurs illimités<br>• Tableau de bord")
    st.button("Choisir Entreprise", key="btn3")
