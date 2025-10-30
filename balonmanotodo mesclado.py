import streamlit as st
st.set_page_config(page_title="Balon mano", page_icon="🤾‍♀")
pg = st.navigation(["balonhand.py", "reglasyseminales.py", "balonmano3.py", "cosa2.py"])
pg.run("'")

import streamlit as st

#Configuración de la Página de Inicio 
st.set_page_config(
    page_title="Gol-Ego: El Árbitro Virtual de Handball",
    page_icon="./logo_golego.png",
    layout="wide"
)


# SECCIÓN HOME PAGE

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

import streamlit as st
import pandas as pd
import numpy as np

# --- Configuración de la Página ---
st.set_page_config(
    page_title="App de Análisis de Handball",
    page_icon="🤾",
    layout="wide"  # Establece el layout de la página en 'wide'
)

# --- Título Principal ---
st.title("🤾 Análisis y Estadísticas de Handball")
st.markdown("""
    Bienvenido a la aplicación base para el análisis de balonmano. 
    Usa la barra lateral para navegar o seleccionar opciones.
""")

st.divider()

# --- Barra Lateral (Sidebar) ---
st.sidebar.header("Opciones de Navegación y Filtro")

# Ejemplo de selección en la barra lateral
opcion_seleccionada = st.sidebar.selectbox(
    "Selecciona una Sección:",
    ("Inicio", "Estadísticas de Jugadores", "Análisis de Partidos", "Visualización de Datos")
)

# Ejemplo de filtro de equipo (podría usarse para filtrar datos)
equipo_seleccionado = st.sidebar.multiselect(
    "Selecciona Equipos (Base de Datos Ficticia):",
    ['Equipo A', 'Equipo B', 'Equipo C', 'Equipo D'],
    default=['Equipo A', 'Equipo B']
)

# --- Contenido Principal Basado en la Selección ---

if opcion_seleccionada == "Inicio":
    st.header("Página de Inicio")
    st.info("Utiliza las otras secciones para ver datos más específicos de handball.")
    
    st.subheader("Datos Ficticios de Prueba")
    
    # Crear un DataFrame ficticio para demostrar la visualización de datos
    data = {
        'Jugador': ['Juan P.', 'Pedro R.', 'Luis S.', 'Carlos M.'],
        'Goles': [np.random.randint(10, 50) for _ in range(4)],
        'Asistencias': [np.random.randint(5, 30) for _ in range(4)],
        'Lanzamientos_Totales': [np.random.randint(40, 100) for _ in range(4)]
    }
    df_ficticio = pd.DataFrame(data)
    
    st.dataframe(df_ficticio)
    st.caption("Esta es una tabla de datos de jugadores ficticia.")

elif opcion_seleccionada == "Estadísticas de Jugadores":
    st.header("Estadísticas Detalladas de Jugadores 📊")
    st.write(f"Mostrando datos para los equipos: **{', '.join(equipo_seleccionado)}**")
    
    st.warning("Aquí podrías cargar y mostrar datos reales de goles, paradas, efectividad de tiro, etc.")
    
    # Ejemplo de un gráfico (histograma de goles ficticios)
    st.subheader("Distribución de Goles (Ficticia)")
    arr = np.random.normal(loc=25, scale=5, size=100) # Goles simulados
    hist_values, bin_edges = np.histogram(arr, bins=10, range=(0, 50))
    st.bar_chart(pd.DataFrame({'Goles': hist_values}, index=pd.Series(bin_edges[:-1].astype(int))))


elif opcion_seleccionada == "Análisis de Partidos":
    st.header("Análisis Táctico de Partidos ♟️")
    st.error("En esta sección se podría implementar el análisis de rendimiento por partido, zonas de tiro, o mapas de calor.")
    
    # Ejemplo de un slider para filtrar el minuto de juego
    minuto_juego = st.slider(
        "Filtrar por Minuto de Juego:",
        0, 60, (0, 60)
    )
    st.write(f"Analizando entre el minuto **{minuto_juego[0]}** y **{minuto_juego[1]}**.")

elif opcion_seleccionada == "Visualización de Datos":
    st.header("Visualización Avanzada 📈")
    st.success("Esta área es para gráficos interactivos, mapas o dashboards complejos.")
    
    st.write("Puedes usar librerías como Plotly, Altair o Matplotlib aquí.")
    
    # Crear un mapa ficticio (aunque en handball no es típico, sirve de ejemplo)
    st.subheader("Mapa Ficticio (Coordenadas de Lanzamiento)")
    
    # Crear un mapa de puntos ficticio (simulando coordenadas de lanzamiento en la cancha)
    map_data = pd.DataFrame(
        np.random.randn(50, 2) / [50, 50] + [40.73, -73.93], # Coordenadas centradas cerca de NYC (solo para ejemplo)
        columns=['lat', 'lon']
    )
    st.map(map_data, zoom=10) # El zoom se ajustará a los puntos
    st.caption("Ubicaciones de lanzamiento simuladas en la cancha.")

st.divider()

# --- Pie de Página ---
st.markdown("---")
st.markdown("Desarrollado con Streamlit. **¡Comienza a personalizar!**")

import streamlit as st

#Widgets y Lógica Principal

st.title("🤾‍♂️ Simulador de Decisión Arbitral")
st.subheader("Ingresa la situación y Gol-Ego te da la decisión.")

#Datos de Sanciones y Señales
# Diccionario para mapear la decisión a la imagen de la señal
SEÑALES = {
    "Golpe Franco": "senial_golpefranco.png",
    "Exclusión (2 min)": "senial_exclusion.png",
    "Lanzamiento de 7 metros": "senial_7metros.png",
    "Continuar Juego": "logo_golego.png" # Usamos el logo para 'continuar'
}

#ENTRADAS DEL USUARIO

with st.sidebar:
    st.header("Opciones de Simulación")
    
    # Widget 1: Selectbox para la Categoría de la Falta
    tipo_falta = st.selectbox(
        "Categoría de la Falta",
        ["Pasos Ilegales", "Bote Ilegal", "Área de 6 metros", "Falta Agresiva"]
    )

st.markdown("---")


#LÓGICA DE LA APLICACIÓN


