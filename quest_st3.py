import streamlit as st
from streamlit_option_menu import option_menu

# Classe simplifiée pour gérer l'authentification
class Authenticate:
    def __init__(self, credentials):
        self.credentials = credentials

    def login_form(self):
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        if st.button("Se connecter"):
            if username in self.credentials and self.credentials[username]['password'] == password:
                st.session_state["authenticated"] = True
                st.session_state["username"] = username
                return username, True
            else:
                st.session_state["authenticated"] = False
                return None, False
        return None, None

    def logout(self):
        if st.sidebar.button("Déconnexion"):
            st.session_state["authenticated"] = False
            st.sidebar.success("Vous avez été déconnecté avec succès.")

# Configuration des données utilisateur
lesdonneesdescomptes = {
    'admin': {
        'name': 'admin',
        'password': 'admin',
        'roles': ['admin']
    },
}

# Initialisation de l'état
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "username" not in st.session_state:
    st.session_state["username"] = None

# Création de l'authentificateur
authenticator = Authenticate(credentials=lesdonneesdescomptes)

# Si l'utilisateur est connecté
if st.session_state["authenticated"]:
    with st.sidebar:
        # Menu latéral
        selection = option_menu(
            menu_title="Menu",
            options=["Accueil", "Les photos de mon chat"],
            icons=["house", "camera"],
            menu_icon="menu-app",
            default_index=0
        )
        # Bouton de déconnexion
        authenticator.logout()

    # Affichage des pages en fonction de la sélection
    if selection == "Accueil":
        st.title("Bienvenue sur ma page")
        st.image("https://media.tenor.com/mq70mIk5Z2oAAAAe/hassan-cehef.png", caption="Bienvenue !")
    elif selection == "Les photos de mon chat":
        st.title("Bienvenue sur l'autre page")
        st.write("Voici une autre page avec des colonnes et des images.")

        # Colonnes avec des images
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg")

        with col2:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg")

        with col3:
            st.header("An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg")

# Si l'utilisateur n'est pas authentifié
else:
    st.title("Connexion")
    name, authentication_status = authenticator.login_form()

    if authentication_status is False:
        st.error("Nom d'utilisateur ou mot de passe incorrect.")
    elif authentication_status is None:
        st.warning("Veuillez entrer votre nom d'utilisateur et votre mot de passe.")
