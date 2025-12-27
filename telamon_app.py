import streamlit as st
import json
import os

# Configuração da Página
st.set_page_config(
    page_title="Telamon Datapad",
    page_icon="💠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilização
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #c9d1d9; }
    h1, h2, h3, h4 { color: #58a6ff; font-family: 'Helvetica Neue', sans-serif; }
    .stTabs [data-baseweb="tab-list"] { gap: 2px; }
    .stTabs [data-baseweb="tab"] { background-color: #161b22; border-radius: 4px 4px 0 0; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { background-color: #21262d; border-bottom: 2px solid #58a6ff; }
    .log-card { background-color: #161b22; padding: 15px; border-radius: 8px; border-left: 4px solid #58a6ff; margin-bottom: 15px; }
    div[data-testid="stExpander"] div[role="button"] p { font-size: 1rem; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

# Função de carga
@st.cache_data
def load_data():
    file_name = 'telamon_protocol_db.json'
    if not os.path.exists(file_name):
        return None
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)

data = load_data()

st.title("💠 Telamon Interface")
if not data:
    st.error("⚠️ ERRO: Banco de dados não encontrado.")
    st.stop()

# Sidebar
with st.sidebar:
    st.header("👤 Perfil")
    meta = data.get("meta_dados", {})
    st.write(f"**Usuário:** {meta.get('usuario')}")
    st.write(f"**Status:** {meta.get('status')}")
    st.caption(f"Versão: {meta.get('versao_protocolo')}")

# Abas Principais
tab_sys, tab_plan, tab_base, tab_bio, tab_res = st.tabs(["✨ Sistemas", "🪐 Planetas", "🏠 Bases", "🧬 Fauna", "⛏️ Recursos"])

# --- SISTEMAS ---
with tab_sys:
    p = data["protocolos"]["sistemas_estelares"]
    st.subheader(f"📡 {p['nome_protocolo']}")
    st.info(f"Formato: `{p['formato']}`")
    
    # Sub-abas de Sistemas
    sub_t1, sub_t2, sub_t3 = st.tabs(["Temas & Cores", "Tática & Economia", "💡 Léxico"])
    
    with sub_t1:
        st.write(p["temas_por_classe_estelar"])
    with sub_t2:
        st.write(p["codigos_taticos"])
    with sub_t3:
        st.markdown("### Inspiração para Nomes")
        lex = p.get("lexico_inspiracao", {})
        for cat, terms in lex.items():
            with st.expander(cat.replace("_", " ").upper()):
                st.code(", ".join(terms), language="text")

# --- PLANETAS ---
with tab_plan:
    p = data["protocolos"]["planetas"]
    st.subheader(f"🌍 {p['nome_protocolo']}")
    st.info(f"Formato: `{p['formato']}`")
    
    sub_t1, sub_t2 = st.tabs(["Códigos de Bioma", "💡 Léxico"])
    
    with sub_t1:
        st.table(p["codigos_bioma"])
        if "sufixos_adicionais" in p:
            st.write("Sufixos Extras:", p["sufixos_adicionais"])
            
    with sub_t2:
        st.markdown("### Inspiração por Bioma")
        lex = p.get("lexico_inspiracao", {})
        for cat, terms in lex.items():
            with st.expander(cat.replace("_", " ").upper()):
                st.code(", ".join(terms), language="text")

# --- BASES ---
with tab_base:
    p = data["protocolos"]["bases"]
    st.subheader(f"🏰 {p['nome_protocolo']}")
    st.table(p["codigos_funcao"])

# --- FAUNA ---
with tab_bio:
    p = data["protocolos"]["xenobiologia"]
    st.subheader(f"🧬 {p['nome_protocolo']}")
    st.warning(f"Formato: `{p['formato']}`")
    
    # Sub-abas agora incluem o Léxico
    bt1, bt2, bt3, bt4, bt5 = st.tabs(["Terrestre", "Fito-Fauna", "Marinha", "Sufixos", "💡 Léxico"])
    
    with bt1:
        st.markdown("#### 🐾 Fauna Terrestre")
        for k, v in p["fauna_terrestre"].items():
            with st.expander(k.title()): st.table(v)
            
    with bt2:
        st.markdown("#### 🌿 Animais-Planta")
        if "fauna_hibrida_planta" in p:
            for k, v in p["fauna_hibrida_planta"].items():
                st.table(v)
        else:
            st.info("Nenhuma fito-fauna registrada ainda.")

    with bt3:
        st.markdown("#### 🌊 Fauna Marinha")
        for k, v in p["fauna_marinha"].items():
            with st.expander(k.title()): st.table(v)
            
    with bt4:
        st.markdown("#### 🏷️ Sufixos")
        st.write(p["sufixos_descritivos"])
        
    with bt5:
        st.markdown("### Inspiração para Criaturas")
        lex = p.get("lexico_inspiracao", {})
        for cat, terms in lex.items():
            with st.expander(cat.replace("_", " ").upper()):
                st.code(", ".join(terms), language="text")

# --- RECURSOS ---
with tab_res:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🌿 Botânica (Gaia)")
        st.write(data["protocolos"]["botanica"]["categorias"])
    with col2:
        st.markdown("### 🪨 Geologia (Lithos)")
        st.write(data["protocolos"]["geologia"]["categorias"])

st.divider()
st.caption(f"ID: {data['meta_dados']['usuario']} // Conectado")