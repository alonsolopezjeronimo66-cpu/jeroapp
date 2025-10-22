import streamlit as st
from PIL import Image

st.title("Aplicaciones de Inteligencia Artificial.")

# --- SIDEBAR ---
with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial.")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

# --- ENLACE PRINCIPAL ---
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Haz clic aquí]({url_ia})")

# --- COLUMNAS PRINCIPALES ---
col1, col2, col3 = st.columns(3)

# ======================== COLUMNA 1 ========================
with col1:
    # Estilo personalizado (azul futbolero)
    st.markdown("""
        <style>
        .main {
            background-color: #001F3F;
            color: white;
            font-family: 'Poppins', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 24px;
            color: #00BFFF;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .stButton > button {
            background-color: #0074D9;
            color: white;
            border: none;
            padding: 0.6em 2em;
            border-radius: 10px;
            font-size: 16px;
            transition: 0.3s;
            font-weight: bold;
        }
        .stButton > button:hover {
            background-color: #00BFFF;
            transform: scale(1.05);
        }
        </style>
    """, unsafe_allow_html=True)

    # --- Sección Conversión de texto a voz ---
    st.markdown('<div class="title">⚽ Intro </div>', unsafe_allow_html=True)
    image = Image.open('txt_to_audio2.png')
    st.image(image, width=250, caption="Transforma tus palabras en voz con IA")
    st.write("Usa una aplicación de **Inteligencia Artificial** para convertir texto en voz fácilmente:")
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("Ir a la página introductoria 🚀"):
        st.markdown("<meta http-equiv='refresh' content='0; url=https://introjeronimo.streamlit.app/'>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Reconocimiento de Objetos ---
    st.subheader("Reconocimiento de Objetos")
    image = Image.open('txt_to_audio.png')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos cómo se detectan objetos en imágenes.") 
    url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    st.write(f"YOLO: [Enlace]({url})")

    # --- Entrenando Modelos ---
    st.subheader("Entrenando Modelos")
    image = Image.open('OIG5.jpg')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos cómo puedes usar tu modelo entrenado.") 
    url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    st.write(f"Modelos: [Enlace]({url})")

# ======================== COLUMNA 2 ========================
with col2:
    st.subheader("Conversión de voz a texto")
    image = Image.open('OIG8.jpg')
    st.image(image, width=200)
    st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
    url = "https://traductor-ab0sp9f6fi.streamlit.app/"
    st.write(f"Voz a texto: [Enlace]({url})")

    st.subheader("Análisis de Datos")
    image = Image.open('data_analisis.png')
    st.image(image, width=190)
    st.write("En la siguiente enlace veremos cómo se pueden analizar datos usando agentes.") 
    url = "https://asistpy-csv.streamlit.app/"
    st.write(f"Datos: [Enlace]({url})")

    st.subheader("Transcriptor Audio y Video")
    image = Image.open('OIG3.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos cómo realizamos transcripciones de audio/video.") 
    url = "https://transcript-whisper.streamlit.app/"
    st.write(f"Transcriptor: [Enlace]({url})")

# ======================== COLUMNA 3 ========================
with col3:
    st.subheader("Generación en Contexto")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
    url = "https://chatpdf-cc.streamlit.app/"
    st.write(f"RAG: [Enlace]({url})")

    st.subheader("Análisis de Imagen")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos la capacidad de análisis en imágenes.") 
    url = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"Visión: [Enlace]({url})")

    st.subheader("Sistema Ciberfísico")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
    url = "https://vision2-gpt4o.streamlit.app/"
    st.write(f"Sistema: [Enlace]({url})")



