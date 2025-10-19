import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# --- CONFIGURACIÓN DE LA PÁGINA ---
# Esto debe ser lo primero que se ejecute en tu script.
st.set_page_config(
    page_title="Maia 💖",
    page_icon="✨",
    layout="wide", # Usa el ancho completo de la página
    initial_sidebar_state="collapsed", # Oculta la barra lateral por defecto
)

# --- CARGAR EL HTML ---
# Abre el archivo HTML que creamos y guárdalo en una variable.
# Usa rutas relativas basadas en la ubicación de este script para evitar errores
# cuando se ejecuta desde otros directorios.
html_path = Path(__file__).resolve().parent / "index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html_code = f.read()

# --- MOSTRAR EL HTML EN STREAMLIT ---
# Renderiza el código HTML dentro de la aplicación.
# Le damos un alto generoso para que ocupe buena parte de la pantalla y activamos el scroll.
components.html(html_code, height=1200, scrolling=True)
