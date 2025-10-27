# Importar streamlit
import streamlit as st

# Configurar la pagina
st.set_page_config(
    page_title="World of Warcraft",
    page_icon=":yellow_heart:", # Usar el comando python -m rich.emoji para ver lista de emojis
    layout="centered",
)

# Configuración de Logo
st.logo(
    "logo_content.png",
)

pg = st.navigation(["Home.py", "Shaman_Enhancement.py"])
pg.run()