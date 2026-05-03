import streamlit as st

# ======================
# CONFIGURACIÓN
# ======================
st.set_page_config(
    page_title="Mis Apps - Portafolio",
    page_icon="🚀",
    layout="wide"
)

# ======================
# ESTILOS
# ======================
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

h1, h2, h3 {
    color: #146AEF;
}

.card {
    background-color: #1E222A;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #2C2F36;
    transition: 0.3s;
}

.card:hover {
    border: 1px solid #146AEF;
    transform: scale(1.02);
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
</style>
""", unsafe_allow_html=True)

# ======================
# HEADER
# ======================
st.title("🚀 Mis Apps en Streamlit")
st.markdown("Explora todas mis aplicaciones desarrolladas con IA y herramientas interactivas.")

st.markdown("---")

# ======================
# LISTA DE APPS (EJEMPLO)
# ======================
apps = [
    {
        "name": "App 1 - RAG PDF",
        "description": "Analiza documentos PDF usando IA.",
        "url": "https://tu-app-1.streamlit.app"
    },
    {
        "name": "App 2 - Generador de Ideas",
        "description": "Crea ideas creativas automáticamente.",
        "url": "https://tu-app-2.streamlit.app"
    },
    {
        "name": "App 3 - Chatbot",
        "description": "Chat inteligente con IA.",
        "url": "https://tu-app-3.streamlit.app"
    },
]

# ======================
# GRID DE APPS
# ======================
cols = st.columns(3)

for i, app in enumerate(apps):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="card">
            <h3>{app['name']}</h3>
            <p>{app['description']}</p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button("Abrir App", app["url"])

# ======================
# FOOTER
# ======================
st.markdown("---")
st.caption("Hecho con Streamlit | Portafolio personal")
