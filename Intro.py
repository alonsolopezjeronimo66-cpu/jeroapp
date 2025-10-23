import streamlit as st
from PIL import Image

# --- Configuración general ---
st.set_page_config(page_title="Aplicaciones IA ⚽", layout="wide")

# Fondo azul futbolero
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #e6f0ff; /* azul claro */
}
[data-testid="stSidebar"] {
    background-color: #99ccff; /* azul medio */
}
h1, h2, h3, p {
    color: #002b80; /* azul oscuro */
    text-align: center;
}
button {
    display: block;
    margin: 0 auto;
}

/* ⚽ --- FIX para quitar las líneas de los enlaces --- */
a, a:visited, a:hover, a:active {
    text-decoration: none !important;
    outline: none !important;
    box-shadow: none !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("Aplicaciones ⚽")

with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial ⚽")
    parrafo = "Estas son mis aplicaciones desarrolladas en clase"
    st.write(parrafo)

# --- App: Mi Primera App ---
st.subheader("Mi Primera App")
image = Image.open('arnoldo.jpg')
st.image(image, width=200)
st.write("Esta fue mi primera aplicación desarrollada con Streamlit. ⚽ Un punto de partida en mi camino de exploración con la Inteligencia Artificial, la programación y la creatividad digital.")
st.markdown(
    """
    <a href="https://introjeronimo.streamlit.app/" target="_blank">
        <button style="
            background-color:#0047b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            ⚽ Abrir Mi Primera App
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

# --- Crear columnas alineadas ---
col1, col2, col3 = st.columns([1, 1, 1], gap="large")

# --- Columna 1 ---
with col1:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    st.subheader("Conversión de texto a voz")
    image = Image.open('dayro.jpg')
    st.image(image, width=190)
    st.write("Convierte texto a voz usando Inteligencia Artificial.")
    st.markdown(
        """
        <a href="https://texto-voz.streamlit.app/" target="_blank">
            <button style="
                background-color:#0047b3;
                color:white;
                border:none;
                padding:12px 24px;
                border-radius:8px;
                font-size:16px;
                cursor:pointer;
            ">
                ⚽ Abrir aplicación de Texto a Voz
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Analizador de Sentimientos")
    image = Image.open('mayer.jpg')
    st.image(image, width=200)
    st.write("Analiza si un texto tiene un sentimiento positivo, negativo o neutro.")
    st.markdown(
    """
    <a href="https://oaemt27uwmahmd2hjlpqn3.streamlit.app/" target="_blank">
        <button style="
            background-color:#0047b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            ⚽ Abrir Analizador de Sentimientos
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.subheader("Reconocimiento de Gestos")
    image = Image.open('pedro.jpg')
    st.image(image, width=200)
    st.write("Reconoce gestos humanos usando modelos de visión por computadora.")
    st.markdown(
    """
    <a href="https://recogestosjero-8faufkkywwrtbkzmufjy6c.streamlit.app/" target="_blank">
        <button style="
            background-color:#0047b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            ⚽ Abrir Reconocimiento de Gestos
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.subheader("Interpretación de Objetos en Imagen")
    image = Image.open('cadavid.jpg')
    st.image(image, width=200)
    st.write("Sube una imagen y la IA te dirá qué objetos aparecen en ella.")
    st.markdown(
    """
    <a href="https://visionapp-isa-lpq3fitf2jwnkastes8odi.streamlit.app/" target="_blank">
        <button style="
            background-color:#0047b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            ⚽ Abrir Reconocimiento de Objetos
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.subheader("Control por Voz")
    image = Image.open('gamero.jpg')
    st.image(image, width=200)
    st.write("Controla acciones mediante comandos de voz.")
    st.markdown(
    """
    <a href="https://ctrlvoiceisa.streamlit.app/" target="_blank">
        <button style="
            background-color:#0047b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            ⚽ Abrir Control por Voz
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)


# --- Columna 2 ---
with col2:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    st.subheader("Conversión de Audio a Texto")
    image = Image.open('ruiz.jpg')
    st.image(image, width=200)
    st.write("Convierte audio en texto automáticamente.")
    st.markdown(
    """
    <a href="https://traductorjero.streamlit.app/" target="_blank">
        <button style="
            background-color:#0047b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            ⚽ Abrir aplicación de Audio a Texto
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.subheader("Análisis de Documentos")
    image = Image.open('larry.jpg')
    st.image(image, width=200)
    st.write("Analiza documentos y genera resúmenes con IA.")
    st.markdown(
    """
    <a href="https://textoespjero-8u9fq66zajqurv4auf2jns.streamlit.app/" target="_blank">
        <button style="
            background-color:#0047b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            ⚽ Abrir Análisis de Documentos
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.subheader("Detección de objetos y rostros")
    image = Image.open('vargas.jpg')
    st.image(image, width=200)
    st.write("Detecta rostros en imágenes y escucha los resultados.")
    st.markdown(
    """
    <a href="https://yolojero-bwrxdh68nxq2ouevtvnu4z.streamlit.app/" target="_blank">
        <button style="
            background-color:#0047b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            ⚽ Abrir aplicación de Detección de Rostros
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.subheader("Reconocer el Dibujo")
    image = Image.open('vega.jpg')
    st.image(image, width=200)
    st.write("La IA intenta adivinar qué representa tu dibujo.")
    st.markdown(
    """
    <a href="https://reconnocer-el-dibujo.streamlit.app/" target="_blank">
        <button style="
            background-color:#0047b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            ⚽ Abrir Reconocimiento de Dibujo
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.subheader("Control LED (IoT)")
    image = Image.open('falcao.jpg')
    st.image(image, width=200)
    st.write("Controla luces LED usando tecnología IoT en tiempo real.")
    st.markdown(
    """
    <a href="https://enviarcmqttisa.streamlit.app/" target="_blank">
        <button style="
            background-color:#0047b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            ⚽ Abrir Control LED (IoT)
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)


# --- Columna 3 ---
with col3:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    st.subheader("Reconocimiento Óptico de Caracteres")
    image = Image.open('catano.jpg')
    st.image(image, width=200)
    st.write("Realiza OCR para convertir texto desde imágenes.")
    st.markdown(
    """
    <a href="https://ocr-audiojero.streamlit.app/" target="_blank">
        <button style="
            background-color:#0047b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            ⚽ Abrir Aplicación OCR Final
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.subheader("Análisis de Textos en Inglés")
    image = Image.open('leo.jpg')
    st.image(image, width=200)
    st.write("Analiza textos en inglés e identifica temas o sentimientos.")
    st.markdown(
    """
    <a href="https://mzbpi586atxn6hg9tdgdth.streamlit.app/" target="_blank">
        <button style="
            background-color:#0047b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            ⚽ Abrir Análisis de Textos en Inglés
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.subheader("Chat con PDF")
    image = Image.open('llinas.jpg')
    st.image(image, width=200)
    st.write("Habla con tus documentos PDF gracias a la IA.")
    st.markdown(
    """
    <a href="https://chatpdfjero.streamlit.app/" target="_blank">
        <button style="
            background-color:#0047b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            ⚽ Abrir Chat con PDF
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.subheader("Historia a partir de un Dibujo")
    image = Image.open('maca.jpg')
    st.image(image, width=200)
    st.write("Genera una historia completa a partir de un dibujo infantil.")
    st.markdown(
    """
    <a href="https://historia-infantil.streamlit.app/" target="_blank">
        <button style="
            background-color:#0047b3;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        ">
            ⚽ Abrir Historia a partir de un Dibujo
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)
