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
