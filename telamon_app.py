import streamlit as st
import json
import os

# Configuração da Página (Deve ser a primeira chamada Streamlit)
st.set_page_config(
    page_title="Telamon Datapad",
    page_icon="💠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilização Customizada (CSS para parecer uma interface Sci-Fi simples)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #c9d1d9;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #161b22;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #21262d;
        border-bottom: 2px solid #58a6ff;
    }
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #58a6ff;
    }
    .metric-card {
        background-color: #161b22;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #30363d;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Função para carregar os dados
@st.cache_data
def load_data():
    file_name = 'telamon_protocol_db.json'
    if not os.path.exists(file_name):
        return None
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)

# Carregamento
data = load_data()

# Cabeçalho do App
st.title("💠 Telamon Interface")

if not data:
    st.error("⚠️ ERRO CRÍTICO: Banco de dados 'telamon_protocol_db.json' não encontrado.")
    st.info("Certifique-se de que o arquivo JSON está no mesmo diretório deste script.")
    st.stop()

# Sidebar com Perfil
with st.sidebar:
    st.header("👤 Perfil do Viajante")
    meta = data.get("meta_dados", {})
    st.write(f"**Usuário:** {meta.get('usuario', 'Desconhecido')}")
    st.write(f"**Status:** {meta.get('status', 'N/A')}")
    st.write(f"**Versão:** {meta.get('versao_protocolo', '1.0')}")
    st.divider()
    st.caption("Sistema Operacional Telamon v5.4")

# Corpo Principal - Abas de Navegação
tab_sistemas, tab_planetas, tab_bases, tab_bio, tab_recursos = st.tabs([
    "✨ Sistemas", "🪐 Planetas", "🏠 Bases", "🧬 Fauna", "⛏️ Recursos"
])

# --- ABA SISTEMAS ---
with tab_sistemas:
    proto = data["protocolos"]["sistemas_estelares"]
    st.subheader(f"📡 {proto['nome_protocolo']}")
    st.info(f"📝 **Formato:** `{proto['formato']}`")
    
    with st.expander("🌟 Temas por Cor de Estrela", expanded=True):
        cols = st.columns(2)
        for idx, (classe, temas) in enumerate(proto["temas_por_classe_estelar"].items()):
            with cols[idx % 2]:
                st.markdown(f"**{classe.replace('_', ' ').title()}**")
                st.code(", ".join(temas))

    with st.expander("📊 Códigos Táticos (Economia & Raça)"):
        st.markdown("**Raças:**")
        st.table(proto["codigos_taticos"]["raca"])
        st.markdown("**Tipo de Economia:**")
        st.json(proto["codigos_taticos"]["tipo_economia"])

# --- ABA PLANETAS ---
with tab_planetas:
    proto = data["protocolos"]["planetas"]
    st.subheader(f"🌍 {proto['nome_protocolo']}")
    st.info(f"📝 **Formato:** `{proto['formato']}`")
    
    st.markdown("### Códigos de Bioma")
    for codigo, desc in proto["codigos_bioma"].items():
        st.markdown(f"- **`{codigo}`** : {desc}")
    
    st.markdown("---")
    st.caption("Sufixos Extras: " + ", ".join([f"`{k}` ({v})" for k, v in proto.get("sufixos_adicionais", {}).items()]))

# --- ABA BASES ---
with tab_bases:
    proto = data["protocolos"]["bases"]
    st.subheader(f"🏰 {proto['nome_protocolo']}")
    st.info(f"📝 **Formato:** `{proto['formato']}`")
    
    st.markdown("### Códigos de Função")
    # Exibir como cartões simples para leitura rápida no celular
    col1, col2 = st.columns(2)
    items = list(proto["codigos_funcao"].items())
    half = len(items) // 2
    
    with col1:
        for k, v in items[:half]:
            st.markdown(f"**`{k}`**\n\n{v}")
    with col2:
        for k, v in items[half:]:
            st.markdown(f"**`{k}`**\n\n{v}")

# --- ABA XENOBIOLOGIA (FAUNA) ---
with tab_bio:
    proto = data["protocolos"]["xenobiologia"]
    st.subheader(f"🧬 {proto['nome_protocolo']}")
    st.warning(f"📝 **Formato:** `{proto['formato']}`")
    
    bio_tabs = st.tabs(["Terrestre", "Marinha", "Sufixos"])
    
    with bio_tabs[0]:
        st.markdown("#### 🐾 Fauna Terrestre")
        for categoria, itens in proto["fauna_terrestre"].items():
            with st.expander(f"{categoria.replace('_', ' ').title()}"):
                st.table(itens)
                
    with bio_tabs[1]:
        st.markdown("#### 🌊 Fauna Marinha")
        for categoria, itens in proto["fauna_marinha"].items():
            with st.expander(f"{categoria.replace('_', ' ').title()}"):
                st.table(itens)

    with bio_tabs[2]:
        st.markdown("#### 🏷️ Sufixos Descritivos")
        for tipo, sufixos in proto["sufixos_descritivos"].items():
            st.markdown(f"**{tipo.replace('_', ' ').title()}**")
            st.json(sufixos)

# --- ABA RECURSOS (BOTANICA E GEOLOGIA) ---
with tab_recursos:
    # Botânica
    st.markdown("### 🌿 Botânica (Protocolo Gaia)")
    proto_bot = data["protocolos"]["botanica"]
    with st.expander("🌲 Árvores & Plantas de Recurso"):
        st.write("**Árvores de Carbono:**")
        st.json(proto_bot["arvores_carbono"])
        st.write("**Plantas Perigosas:**")
        st.json(proto_bot["flora_perigosa"])
    
    st.divider()
    
    # Geologia
    st.markdown("### 🪨 Geologia (Protocolo Lithos)")
    proto_geo = data["protocolos"]["geologia"]
    with st.expander("💎 Minerais & Curiosidades"):
        st.write("**Ferrita Básica:**")
        st.json(proto_geo["ferrita_basica"])
        st.write("**Minerais Avançados:**")
        st.json(proto_geo["minerais_avancados"])

# Rodapé
st.markdown("---")
st.caption(f"📡 Conexão Telamon Estabelecida. ID: {data['meta_dados']['usuario']}")