import streamlit as st

#Widgets y Lógica Principal

st.title("🤾‍♂️ Simulador de Decisión Arbitral")
st.subheader("Ingresa la situación y Gol-Ego te da la decisión.")

#Datos de Sanciones y Señales
# Diccionario para mapear la decisión a la imagen de la señal
SEÑALES = {
    "Golpe Franco": "./assets/senial_golpefranco.png",
    "Exclusión (2 min)": "./assets/senial_exclusion.png",
    "Lanzamiento de 7 metros": "./assets/senial_7metros.png",
    "Continuar Juego": "./assets/logo_golego.png" # Usamos el logo para 'continuar'
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

decision = None
regla = None
senial_clave = None

if tipo_falta == "Pasos Ilegales":
    # Widget 2: Slider para el número de pasos
    num_pasos = st.slider("¿Cuántos pasos dio el jugador con el balón en la mano?", 1, 6, 3)
    
    if num_pasos > 3:
        decision = "FALTA: Pasos Ilegales."
        regla = "El reglamento solo permite un máximo de 3 pasos antes o después de botar."
        senial_clave = "Golpe Franco"
    else:
        decision = "Juego Válido."
        regla = "El jugador dio 3 o menos pasos. La jugada puede continuar."
        senial_clave = "Continuar Juego"
        
elif tipo_falta == "Bote Ilegal":
    # Widget 3: Checkbox
    rebote = st.checkbox("¿El jugador realizó un doble bote (botó, agarró con dos manos y volvió a botar)?")
    
    if rebote:
        decision = "FALTA: Doble Bote Ilegal."
        regla = "Una vez que el jugador detiene el bote agarrando el balón con ambas manos, no puede volver a botar. Debe pasar o lanzar."
        senial_clave = "Golpe Franco"
    else:
        decision = "Juego Válido."
        regla = "El bote fue reglamentario."
        senial_clave = "Continuar Juego"

elif tipo_falta == "Área de 6 metros":
    # Widget 4: Radio para la ubicación de la falta
    ubicacion = st.radio(
        "¿Dónde pisó el atacante?",
        ["Fuera del área (válido)", "Línea del área (válido)", "Dentro del área (invasión)"]
    )
    
    if ubicacion == "Dentro del área (invasión)":
        decision = "FALTA: Invasión del Área de Portería."
        regla = "Un jugador de campo no puede pisar el área de 6 metros. El portero es el único autorizado."
        senial_clave = "Golpe Franco"
    else:
        decision = "Juego Válido."
        regla = "Es válido pisar la línea del área (considerado fuera) o no pisarla."
        senial_clave = "Continuar Juego"

elif tipo_falta == "Falta Agresiva":
    # Widget 5: Selectbox para el nivel de agresión
    agresion = st.selectbox(
        "Nivel de Contacto",
        ["Forcejeo normal", "Sujeción/Empujón repetitivo", "Contacto directo a la cabeza/cuello"]
    )
    
    if agresion == "Contacto directo a la cabeza/cuello":
        decision = "SANCIÓN GRAVE: Exclusión."
        regla = "Todo contacto con riesgo de lesión o falta intencional requiere al menos dos minutos de exclusión."
        senial_clave = "Exclusión (2 min)"
    elif agresion == "Sujeción/Empujón repetitivo":
        decision = "SANCIÓN LEVE: Amonestación (Tarjeta Amarilla)."
        regla = "Señala una conducta incorrecta que podría escalar."
        senial_clave = "Golpe Franco" # O se podría usar una señal de amonestación si se tuviera la imagen
    else:
        decision = "Juego Válido."
        regla = "El forcejeo es parte del juego. No se requiere sanción."
        senial_clave = "Continuar Juego"


#RESULTADO DE LA APLICACIÓN
st.markdown("# Resultado y Decisión")
if decision:
    if "FALTA" in decision or "SANCIÓN" in decision:
        st.error(f" **DECISIÓN ARBITRAL:** {decision}")
        st.info(f"**REGLA APLICADA:** {regla}")
    else:
        st.success(f" **DECISIÓN ARBITRAL:** {decision}")
        st.info(f"**REGLA APLICADA:** {regla}")
        
    st.markdown("---")
    
    st.markdown(f"### Señal de Arbitraje: {senial_clave}")
    
    # Muestra la imagen de la señal correspondiente
    if senial_clave in SEÑALES:
        st.image("oip8.jpg", caption=senial_clave, width=250)



