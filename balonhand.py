import streamlit as st

#Configuración de la Página de Inicio 
st.set_page_config(
    page_title="Gol-Ego: El Árbitro Virtual de Handball",
    page_icon="descarga.jpg",
    layout="wide"
)

#Ruta a la Imagen del Logo
LOGO_PATH = "OIP5.jpg"


# SECCIÓN HOME PAGE

st.image("OIP5.jpg")
st.title("GOL-EGO: Tu Guía Rápida de Reglas de Handball")
st.markdown("---")

#Problema a Resolver 
st.header("1. El Problema: Confusión en la Cancha ")
st.write("""
El balonmano (handball) es un deporte rápido y dinámico, pero sus reglas específicas 
(como el límite de pasos, el tiempo de posesión y las sanciones) a menudo confunden 
a jugadores novatos, padres, entrenadores en formación y árbitros principiantes. 
Una decisión equivocada puede cambiar el curso de un partido y generar frustración.
**Necesitamos una referencia rápida e interactiva, ¡no un manual de 300 páginas!**
""")

st.markdown("---")

#Usuario Objetivo}
st.header("2. Nuestro Usuario: El Novato Entusiasta")
st.subheader("Perfil: Juan, el Futuro Árbitro")
st.write("""
- **Edad:** 16 años.
- **Ubicación:** Estudiante de educación física que recién comienza a arbitrar partidos de ligas escolares.
- **Estilo de Vida:** Activo, siempre con su teléfono para revisar información deportiva.
- **Problema:** En el calor del juego, olvida la señal de arbitraje correcta o duda si la falta amerita un 'Golpe Franco' o una 'Exclusión'.
""")

st.markdown("---")

#Solución de la Aplicación
st.header("3. La Solución: Gol-Ego al Rescate ")
st.write("""
**Gol-Ego** es una aplicación web intuitiva desarrollada en Python y Streamlit que sirve 
como un **árbitro virtual de bolsillo**. Permite al usuario simular situaciones de juego 
mediante entradas sencillas (sliders y menús) y devuelve instantáneamente la decisión 
reglamentaria y la señal de arbitraje visual correcta.

*¡Nunca más dudarás de la regla de los 3 pasos!*

""")

st.image("OIP2.jpg")
st.image("OIP1.jpg")
st.image("juego-de-balonmano.jpg")

st.video("https://youtu.be/QxyPbPZxf9A?si=vQ94k8VVCBWLjRZN")



