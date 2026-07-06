import streamlit as st
import google.generativeai as genai

# Configuration de la page
st.title("LINKA - Votre portail d'accès intelligent")

# Récupération de la clé depuis les Secrets (il faut que ce nom soit identique à celui dans Streamlit)
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# Initialisation du modèle
model = genai.GenerativeModel('gemini-pro')

# Interface utilisateur
user_input = st.text_input("Que cherches-tu ?")

if user_input:
    try:
        response = model.generate_content(user_input)
        st.write(response.text)
    except Exception as e:
        st.error(f"Une erreur est survenue : {e}")
