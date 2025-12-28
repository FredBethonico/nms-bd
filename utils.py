# Nome do arquivo: utils.py
import streamlit as st
import json
import os

def carregar_dados():
    """
    Função responsável por ler o arquivo JSON.
    Retorna os dados se der certo, ou None se falhar.
    """
    file_name = 'telamon_protocol_db.json'
    
    # Verifica se o arquivo existe antes de tentar abrir
    if not os.path.exists(file_name):
        st.error(f"⚠️ ERRO CRÍTICO: O arquivo '{file_name}' não foi encontrado.")
        return None
        
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        st.error("⚠️ ERRO: O arquivo JSON está corrompido ou mal formatado.")
        return None

def aplicar_estilo():
    """
    Função que guarda todo o CSS para deixar o código principal mais limpo.
    """
    st.markdown("""
        <style>
        .stApp { background-color: #0e1117; color: #c9d1d9; }
        h1, h2, h3, h4 { color: #58a6ff; font-family: 'Helvetica Neue', sans-serif; }
        
        /* Ajuste das Abas */
        .stTabs [data-baseweb="tab-list"] { gap: 2px; }
        .stTabs [data-baseweb="tab"] { background-color: #161b22; border-radius: 4px 4px 0 0; }
        .stTabs [data-baseweb="tab"][aria-selected="true"] { background-color: #21262d; border-bottom: 2px solid #58a6ff; }
        
        /* Caixas de texto e expanders */
        .log-card { background-color: #161b22; padding: 15px; border-radius: 8px; border-left: 4px solid #58a6ff; margin-bottom: 15px; }
        div[data-testid="stExpander"] div[role="button"] p { font-size: 1rem; font-weight: 600; }
        </style>
    """, unsafe_allow_html=True)