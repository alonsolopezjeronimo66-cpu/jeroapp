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
   st.subheader("⚽ Mi Primera App: De Texto a Voz Azul Futbolero")

    image = Image.open('OIG5.jpg')
    st.image(image, width=190)

    st.write(
    """
    ¡Bienvenido a mi primera aplicación del repositorio!  
    Esta herramienta convierte cualquier texto en voz usando Inteligencia Artificial.  
    Su diseño y espíritu están inspirados en la pasión futbolera — azul, fuerte y siempre en movimiento. 💙  
    Perfecta para narrar tus ideas, mensajes o incluso tus cánticos favoritos del estadio.
    """
    )

    # Botón azul futbolero
    st.markdown(
    """
    <a href="https://introjeronimo.streamlit.app/">
        <button style="
            background-color:#0047AB;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
            box-shadow:0px 4px 10px rgba(0,0,0,0.2);
        ">
            💙 Probar la App de Texto a Voz
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

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



