import streamlit as st

# Configuration de la page
st.set_page_config(page_title="LINKA", page_icon="🔗")

# Titre de l'application
st.title("🔗 LINKA")
st.write("Bienvenue sur LINKA, votre outil pour accéder directement aux sites web.")

# Zone de recherche
user_input = st.text_input("Quel site cherches-tu ?")

if user_input:
    # Message de confirmation selon tes règles métiers
    st.write(f"Recherche en cours pour : {user_input}...")
    st.info("Je suis là uniquement pour vous aider à trouver des liens vers des sites web.")
