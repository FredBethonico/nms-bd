# Nome do arquivo: abas.py
import streamlit as st
import pandas as pd


# --- SISTEMAS ---
def exibir_sistemas(data):
    p = data["protocolos"]["sistemas_estelares"]
    st.subheader(f"📡 {p['nome_protocolo']}")
    st.info(f"Formato: `{p['formato']}`")
    
    sub_t1, sub_t2 = st.tabs(["Temas & Cores", "Tática & Economia"])
    
    # Tab 1: Temas & Cores
    with sub_t1: 
        for star_class, themes in p["temas_por_classe_estelar"].items():
            clean_name = star_class.replace("_", " ").title()
            with st.expander(f"{clean_name}", expanded=False):
                st.markdown(" ".join([f"`{t}`" for t in themes]))

    # Tab 2: Tática & Economia
    with sub_t2: 
        tacs = p["codigos_taticos"]
        
        with st.expander("👽 Raças", expanded=True):
            for k, v in tacs["raca"].items():
                st.markdown(f"- **`{k}`**: {v}")
        
        with st.expander("🏭 Tipos de Economia", expanded=True):
            for k, v in tacs["tipo_economia"].items():
                st.markdown(f"- **`{k}`**: {v}")
                
        with st.expander("💰 Tiers de Economia", expanded=True):
            for k, v in tacs["economia_tier"].items():
                st.markdown(f"- **`{k}`**: {v}")
               
               
               
# --- PLANETAS ---
def exibir_planetas(data):
    p = data["protocolos"]["planetas"]
    st.subheader(f"🌍 {p['nome_protocolo']}")
    st.info(f"Formato: `{p['formato']}`")
    
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

# --- BASES ---
def exibir_bases(data):
    p = data["protocolos"]["bases"]
    st.subheader(f"🏰 {p['nome_protocolo']}")
    st.info(f"Formato: `{p['formato']}`")
    
    df_bases = pd.DataFrame(
        list(p["codigos_funcao"].items()),
        columns=["Código", "Função"]
    )
    st.table(df_bases)

# --- FAUNA ---
def exibir_fauna(data):
    p = data["protocolos"]["xenobiologia"]
    st.subheader(f"🧬 {p['nome_protocolo']}")
    st.info(f"Formato: `{p['formato']}`")
    
    bt1, bt2, bt3, bt4, bt5 = st.tabs(["Terrestre", "Fito-Fauna", "Marinha", "Sufixos", "Léxico"])
    
    # Tab 1: Fauna Terrestre
    with bt1:
        st.markdown("#### 🐾 Fauna Terrestre")
        for k, v in p["fauna_terrestre"].items():
            with st.expander(k.replace("_", " ").title()): 
                st.table(
                    pd.DataFrame(
                        list(v.items()), 
                        columns=["Prefixo", "Descrição"]
                    )
                )
           
    # Tab 2: Fito-Fauna 
    with bt2:
        st.markdown("#### 🌿 Fito-Fauna")
        for k, v in p["fauna_hibrida_planta"].items():
            with st.expander(k.replace("_", " ").title()):  
                st.table(
                    pd.DataFrame(
                        list(v.items()), 
                        columns=["Prefixo", "Descrição"]
                    )
                )

    # Tab 3: Fauna Marinha
    with bt3:
        st.markdown("#### 🌊 Fauna Marinha")
        for k, v in p["fauna_marinha"].items():
            with st.expander(k.replace("_", " ").title()):  
                st.table(
                    pd.DataFrame(
                        list(v.items()), 
                        columns=["Prefixo", "Descrição"]
                    )
                )
          
    # Tab 4: Sufixos Descritivos        
    with bt4:
        st.markdown("#### 🏷️ Sufixos")
        for k, v in p["sufixos_descritivos"].items():
            with st.expander(k.replace("_", " ").title()):  
                st.table(
                    pd.DataFrame(
                        list(v.items()), 
                        columns=["Sufixo", "Descrição"]
                    )
                )
                
    # Tab 5: Léxico        
    with bt5:
        st.markdown("### Inspiração para Criaturas")
        lex = p.get("lexico_inspiracao", {})
        for cat, terms in lex.items():
            with st.expander(cat.replace("_", " ").title()): 
                st.markdown(" ".join([f"`{t}`" for t in terms]))
                
# --- LEXICO ---
def lexico_criativo(data):
    p = data["protocolos"]["lexico_inspiracao_sistemas_mundos"]
    st.subheader("✒️ Léxico Criativo")
            
    t1, t2, t3, t4, t5 = st.tabs(["Tematicos", "Biomas", "Economia", "Conflito", "Lore"])
    
    # Tab 1: Temáticos
    with t1:
        st.markdown("### Temáticos")
        lex = p.get("tematicos", {})
        for cat, terms in lex.items():
            with st.expander(cat.replace("_", " ").title()): 
                st.markdown(" ".join([f"`{t}`" for t in terms]))
    
    # Tab 2: Biomas
    with t2:
        st.markdown("### Biomas")
        lex = p.get("biomas", {})
        for cat, terms in lex.items():
            with st.expander(cat.replace("_", " ").title()):
                st.markdown(" ".join([f"`{t}`" for t in terms]))
    
    # Tab 3: Economia
    with t3:
        st.markdown("### Economia")
        lex = p.get("economia", {})
        for cat, terms in lex.items():
            with st.expander(cat.replace("_", " ").title()):
                st.markdown(" ".join([f"`{t}`" for t in terms]))
    
    # Tab 4: Conflito
    with t4:
        st.markdown("### Conflito")
        lex = p.get("conflito-ameaca", {})
        for cat, terms in lex.items():
            with st.expander(cat.replace("_", " ").title()):
                st.markdown(" ".join([f"`{t}`" for t in terms]))
                
    # Tab 5: Lore
    with t5:
        st.markdown("### Lore")
        lex = p.get("lore", {})
        for cat, terms in lex.items():
            with st.expander(cat.replace("_", " ").title()):
                st.markdown(" ".join([f"`{t}`" for t in terms]))