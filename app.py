import streamlit as st
import google.generativeai as genai
import os

# Configuration de la page
st.set_page_config(page_title="LINKA", page_icon="🔗", layout="wide")

# Configuration de l'IA (utilise la clé définie dans les secrets Streamlit)
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

# CSS (ton style actuel)
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); color: white; }
</style>
""", unsafe_allow_html=True)

# Interface
st.markdown("<h1 style='text-align: center;'>🔗 LINKA - Votre portail d'accès intelligent</h1>", unsafe_allow_html=True)

# Zone de recherche
user_input = st.text_input("Quel site cherches-tu ?")

if user_input:
    with st.spinner('Recherche en cours...'):
        response = model.generate_content(f"Trouve le lien officiel ou des informations pertinentes pour : {user_input}")
        st.write("### Résultat :")
        st.write(response.text)

# (Garde ici ta section "Nos Plans d'abonnement" et le code create_card actuel)
