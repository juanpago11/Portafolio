import streamlit as st

# ======================
# CONFIG
# ======================
st.set_page_config(
    page_title="Juan Pablo Gomez | Apps Hub",
    page_icon="🚀",
    layout="wide"
)

# ======================
# ESTILOS PRO
# ======================
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

h1 {
    color: #146AEF;
}

.card {
    background-color: #1E222A;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #2C2F36;
    transition: 0.3s;
    height: 180px;
}

.card:hover {
    border: 1px solid #146AEF;
    transform: scale(1.03);
}

.stButton button {
    width: 100%;
    border-radius: 10px;
    background-color: #146AEF;
    color: white;
    border: none;
    padding: 10px;
}

.stButton button:hover {
    background-color: #0d4fc2;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ======================
# HEADER
# ======================
st.title("Portafolio de Apps - Juan Pablo Gomez")
st.markdown("Explora todas mis aplicaciones desarrolladas en Streamlit")

st.markdown("---")

# ======================
# BUSCADOR
# ======================
search = st.text_input("Buscar app...")

# ======================
# TUS APPS
# ======================
apps = [
    {"name": "Camara Teacher Santi", "url": "https://teachersantigomez-camara.streamlit.app"},
    {"name": "OCR Audio", "url": "https://ocr-audio-audios.streamlit.app"},
    {"name": "Analisis de Sentimientos", "url": "https://sentimenta-3c8yedfvnfxhtfgzvdhbqw.streamlit.app"},
    {"name": "TDF ESP", "url": "https://tdfesp-rzkctu5ddjvm6nkpflvqs7.streamlit.app"},
    {"name": "App Experimental", "url": "https://wtdkiyzuopcmf6zn3yzrfn.streamlit.app"},
    {"name": "Blog Juanpa", "url": "https://tmjuanpablogomez.streamlit.app"},
    {"name": "Traductor", "url": "https://traductor-jptraductor.streamlit.app"},
    {"name": "Tutorial 1", "url": "https://tutorial1-jp.streamlit.app"},
    {"name": "WordCloud", "url": "https://wordcloud-7kszkwvishrtxxrhyy4fyx.streamlit.app"},
    {"name": "YOLO App", "url": "https://yoloyolo.streamlit.app"},
    {"name": "Teacher Santi 2", "url": "https://teachersantigomez-mkmqcrhzzxqszzustwgysn.streamlit.app"},
    {"name": "Generador de Texto", "url": "https://m6hqytafycpguyxsep4cm9.streamlit.app"},
    {"name": "ChatPDF v1", "url": "https://chatpdfjp-cdtkor4vsr7uqcmtjk2nbe.streamlit.app"},
    {"name": "Analisis de Imagen", "url": "https://chatpdfjp-5vrcvomgplt4cn79ntjkwv.streamlit.app"},
    {"name": "Adivina el numero", "url": "https://k8lmcvfjjzsskx2hvqgklf.streamlit.app"},
    {"name": "Tablerito", "url": "https://tableritojp.streamlit.app"},
    {"name": "Animacion", "url": "https://animacion.streamlit.app"},
    {"name": "Receptor MQTT", "url": "https://recepmqtt-ycflymxqfextxujqfyiymf.streamlit.app"},
    {"name": "Sender MQTT", "url": "https://sendcmqtt-khxdd9sdnyxzpxacgud6tm.streamlit.app"},
    {"name": "Control por Voz", "url": "https://ctrlvoice-2vwrbcxcdq5rl27fuyhqbu.streamlit.app"},
]

# ======================
# FILTRO
# ======================
filtered_apps = [
    app for app in apps
    if search.lower() in app["name"].lower()
]

# ======================
# GRID
# ======================
cols = st.columns(3)

for i, app in enumerate(filtered_apps):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="card">
            <h3>{app['name']}</h3>
            <p>Haz clic para abrir la aplicación</p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button("Abrir App", app["url"])

# ======================
# FOOTER
# ======================
st.markdown("---")
st.markdown('<div class="footer">Hecho por Juan Pablo Gomez | Streamlit Apps Hub</div>', unsafe_allow_html=True)
