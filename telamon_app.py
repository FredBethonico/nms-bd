# Nome do arquivo: telamon_app.py
import streamlit as st
# Importamos as nossas "caixas" (módulos)
import utils
import abas

# 1. Configuração da Página (Deve ser sempre o primeiro comando Streamlit)
st.set_page_config(
    page_title="Telamon Datapad",
    page_icon="💠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Carregar Estilos e Dados usando o utils.py
utils.aplicar_estilo()
data = utils.carregar_dados()

# Título Principal
st.title("💠 Sistema de Nomenclatura 💠")

# Se os dados não carregarem, paramos por aqui para evitar erros
if not data:
    st.stop()

# 3. Sidebar (Perfil)
with st.sidebar:
    st.header("👤 Perfil")
    meta = data.get("meta_dados", {})
    st.write(f"**Usuário:** {meta.get('usuario')}")
    st.write(f"**Título:** {meta.get('titulo')}")  
    st.write(f"**Status:** {meta.get('status')}")
    st.caption(f"Versão: {meta.get('versao_protocolo')}")

# 4. Criação das Abas Principais
# Criamos as variáveis para cada aba
tab_sys, tab_plan, tab_base, tab_bio, tab_res = st.tabs([
    "✨ Sistemas", 
    "🪐 Planetas", 
    "🏠 Bases", 
    "🧬 Fauna", 
    "⛏️ Recursos"
])

# 5. Preenchimento das Abas
# Aqui chamamos as funções que criamos no arquivo abas.py
with tab_sys:
    abas.exibir_sistemas(data)

with tab_plan:
    abas.exibir_planetas(data)

with tab_base:
    abas.exibir_bases(data)

with tab_bio:
    abas.exibir_fauna(data)

with tab_res:
    abas.exibir_recursos(data)

# Rodapé
st.divider()
st.caption(f"ID: {data['meta_dados']['usuario']} // Conectado via Modular System")