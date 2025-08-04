import streamlit as st
from datetime import datetime
import time

# Configuración de página
st.set_page_config(page_title="⚠️ ALERTA Inspirafest", layout="centered")

# Fecha objetivo
fecha_evento = datetime(2025, 8, 6, 9, 0, 0)

# CSS con glitch aplicado al contenedor .stApp
st.markdown("""
    <style>
    @keyframes fondoGlitch {
        0% {background-color: #000000;}
        20% {background-color: #111111;}
        40% {background-color: #220000;}
        60% {background-color: #111111;}
        80% {background-color: #330000;}
        100% {background-color: #000000;}
    }

    .stApp {
        animation: fondoGlitch 0.3s infinite;
    }

    .glitch {
        font-size: 50px;
        font-weight: bold;
        color: red;
        text-align: center;
        position: relative;
        animation: glitchAnim 1s infinite;
    }
    @keyframes glitchAnim {
        0% {text-shadow: 2px 0 #00FF00, -2px 0 #FF00FF;}
        20% {text-shadow: -2px -2px #00FF00, 2px 2px #FF00FF;}
        40% {text-shadow: 2px -2px #00FF00, -2px 2px #FF00FF;}
        60% {text-shadow: -2px 2px #00FF00, 2px -2px #FF00FF;}
        80% {text-shadow: 2px 2px #00FF00, -2px -2px #FF00FF;}
        100% {text-shadow: none;}
    }

    .contador {
        font-size: 45px;
        font-weight: bold;
        color: #00FF00;
        text-align: center;
        text-shadow: 0 0 5px #00FF00;
    }

    .mensaje {
        font-size: 20px;
        color: #FF0000;
        text-align: center;
        animation: blink 1.5s infinite;
    }
    @keyframes blink {
        0% {opacity: 1;}
        50% {opacity: 0;}
        100% {opacity: 1;}
    }

    .error-final {
        font-size: 60px;
        font-weight: bold;
        color: yellow;
        text-align: center;
        background-color: red;
        padding: 50px;
        animation: blink 0.5s infinite;
    }
    </style>
""", unsafe_allow_html=True)

# Calcular tiempo restante
ahora = datetime.now()
tiempo_restante = fecha_evento - ahora
segundos_totales = tiempo_restante.total_seconds()

# ALERTA FINAL si quedan menos de 5 segundos
if segundos_totales <= 5 and segundos_totales > 0:
    st.markdown("<div class='error-final'>🚨 ERROR FATAL – ACTIVACIÓN INMEDIATA 🚨</div>", unsafe_allow_html=True)
elif segundos_totales <= 0:
    st.markdown("<div class='contador'>🔥 INSPIRAFEST EN PROGRESO 🔥</div>", unsafe_allow_html=True)
else:
    # Título con glitch
    st.markdown("<div class='glitch'>⚠️ ALERTA CRÍTICA: INSPIRAFEST ⚠️</div>", unsafe_allow_html=True)

    # Contador
    dias = tiempo_restante.days
    horas, resto = divmod(tiempo_restante.seconds, 3600)
    minutos, segundos = divmod(resto, 60)
    st.markdown(f"<div class='contador'>{dias}D : {horas}H : {minutos}M : {segundos}S</div>", unsafe_allow_html=True)

    # Mensajes intensos
    mensajes = [
        "[SISTEMA] ¿Realmente está todo listo?",
        "[ALERTA] última oportunidad de reacción.",
        "[VERIFICACIÓN] ¿Estan todos realmente preparados? ",
        "[SISTEMA] El público está llegando… ¿y ustedes?",
        "[CRÍTICO]  Los Proveedores Confirmaron? .",
        "[ADVERTENCIA] Cada segundo perdido aumenta el riesgo."
    ]
    mensaje_index = (segundos // 3) % len(mensajes)
    st.markdown(f"<div class='mensaje'>{mensajes[mensaje_index]}</div>", unsafe_allow_html=True)

# Refresco
time.sleep(1)
st.rerun()
