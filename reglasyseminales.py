import streamlit as st

st.title(" Referencia Rápida: Cancha y Señales")
st.markdown("---")

#Reglas con Expansión y Contenido Multimedia

st.header("1. El Campo de Juego ")
st.info("Conoce las zonas clave para entender las faltas de invasión.")
st.image("./assets/cancha_handball.jpg", caption="Diagrama Oficial de la Cancha de Handball", use_column_width=True)

st.markdown("---")

st.header("2. Sanciones y Señales ")
st.info("Identifica visualmente la señal correcta que debe hacer el árbitro.")

# Uso de st.expander para organizar la información 
with st.expander("Señal de Golpe Franco"):
    st.write("""
    **¿Cuándo se usa?** Es la sanción más común. Se usa para faltas menores o reglas técnicas no cumplidas (ej. pasos ilegales, doble bote, entrar al área).
    """)
    st.image("./assets/senial_golpefranco.png", width=200, caption="Golpe Franco")

with st.expander("Señal de Lanzamiento de 7 Metros"):
    st.write("""
    **¿Cuándo se usa?** Similar a un penal. Se sanciona cuando una clara ocasión de gol es impedida ilegalmente por la defensa o el portero.
    """)
    st.image("./assets/senial_7metros.png", width=200, caption="Lanzamiento de 7 metros")

with st.expander("Señal de Exclusión (2 minutos)"):
    st.write("""
    **¿Cuándo se usa?** Para faltas más graves, contacto ilegal repetido, o conducta antideportiva. El jugador debe abandonar el campo por 2 minutos.
    """)
    st.image("./assets/senial_exclusion.png", width=200, caption="Exclusión de 2 minutos")

