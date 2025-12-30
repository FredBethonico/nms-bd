# Nome do arquivo: abas.py
import streamlit as st
import pandas as pd


# --- FUNÇÃO PARA A ABA DE SISTEMAS ---
def exibir_sistemas(data):
    p = data["protocolos"]["sistemas_estelares"]
    st.subheader(f"📡 {p['nome_protocolo']}")
    st.info(f"Formato: `{p['formato']}`")
    
    sub_t1, sub_t2, sub_t3 = st.tabs(["Temas & Cores", "Tática & Economia", "Léxico"])
    
    with sub_t1:
        for star_class, themes in p["temas_por_classe_estelar"].items():
            clean_name = star_class.replace("_", " ").title()
            with st.expander(f"{clean_name}", expanded=False):
                st.markdown(" ".join([f"`{t}`" for t in themes]))

    with sub_t2:
        tacs = p["codigos_taticos"]
        st.markdown("##### 👽 Raças")
        cols = st.columns(3)
        for i, (k, v) in enumerate(tacs["raca"].items()):
            cols[i % 3].markdown(f"**`{k}`** : {v}")
            
        st.divider()
        with st.expander("🏭 Tipos de Economia", expanded=True):
            for k, v in tacs["tipo_economia"].items():
                st.markdown(f"- **`{k}`**: {v}")
                
        with st.expander("💰 Tiers de Economia", expanded=False):
            for k, v in tacs["economia_tier"].items():
                st.markdown(f"- **{k}**: {v}")

    with sub_t3:
        st.markdown("### Inspiração para Nomes")
        lex = p.get("lexico_inspiracao", {})
        for cat, terms in lex.items():
            with st.expander(cat.replace("_", " ").upper()):
                st.code(", ".join(terms), language="text")

# --- FUNÇÃO PARA A ABA DE PLANETAS ---
def exibir_planetas(data):
    p = data["protocolos"]["planetas"]
    st.subheader(f"🌍 {p['nome_protocolo']}")
    st.info(f"Formato: `{p['formato']}`")
    
    sub_t1, sub_t2 = st.tabs(["Biomas & Códigos", "Léxico"])
    
    with sub_t1:
        df_biomas = pd.DataFrame(
            list(p["codigos_bioma"].items()),
            columns=["Código de Bioma", "Descrição"]
        )
        st.table(df_biomas)
        
    if "sufixos_adicionais" in p:
        st.markdown("#### Sufixos Extras")
        df_sufixos = pd.DataFrame(
            list(p["sufixos_adicionais"].items()),
            columns=["Sufixo", "Descrição"]
        )
        st.table(df_sufixos)  
            
    with sub_t2:
        st.markdown("### Inspiração por Bioma")
        lex = p.get("lexico_inspiracao", {})
        for cat, terms in lex.items():
            with st.expander(cat.replace("_", " ").upper()):
                st.code(", ".join(terms), language="text")

# --- FUNÇÃO PARA A ABA DE BASES ---
def exibir_bases(data):
    p = data["protocolos"]["bases"]
    st.subheader(f"🏰 {p['nome_protocolo']}")
    st.info(f"Formato: `{p['formato']}`")
    
    df_bases = pd.DataFrame(
        list(p["codigos_funcao"].items()),
        columns=["Código", "Função"]
    )
    st.table(df_bases)

# --- FUNÇÃO PARA A ABA DE FAUNA ---
def exibir_fauna(data):
    p = data["protocolos"]["xenobiologia"]
    st.subheader(f"🧬 {p['nome_protocolo']}")
    st.info(f"Formato: `{p['formato']}`")
    
    bt1, bt2, bt3, bt4, bt5 = st.tabs(["Terrestre", "Fito-Fauna", "Marinha", "Sufixos", "Léxico"])
    
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

# --- FUNÇÃO PARA A ABA DE RECURSOS ---
def exibir_recursos(data):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🌿 Botânica (Gaia)")
        for k, v in data["protocolos"]["botanica"]["categorias"].items():
            st.markdown(f"- **{k}**: {v}")
            
    with col2:
        st.markdown("### 🪨 Geologia (Lithos)")
        for k, v in data["protocolos"]["geologia"]["categorias"].items():
            st.markdown(f"- **{k}**: {v}")