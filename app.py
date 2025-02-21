import streamlit as st
import numpy as np

# Função para entrada de dados
def obter_entrada(mensagem, minimo=0.01):
    return st.number_input(mensagem, min_value=minimo, format="%.2f")

st.title("Análise de Performance da Evaporação")

# Layout com colunas
col1, col2 = st.columns(2)

with col1:
    vazao_lp15 = obter_entrada("Digite a vazão de entrada do 4º efeito (t/h):")
    solidos_secos_entrada = obter_entrada("Digite o teor de sólidos secos do LP15 (%):", 0.1)

with col2:
    temperatura = 94
    solidos_secos_saida = obter_entrada("Digite o teor de sólidos secos do LP80 (%):", 0.1)

if st.button("Calcular"):
    # Cálculos
    densidade = ((997 + 649 * solidos_secos_entrada / 100) * (1 - 0.000369 * (temperatura - 25) - 0.00000194 * (temperatura - 25)**2)) / 1000
    producao_diaria = (vazao_lp15 * densidade * (solidos_secos_entrada / 100)) * 24
    capacidade_agua_evaporada = (1 / 24) * producao_diaria * (100 / solidos_secos_entrada - 100 / solidos_secos_saida)
    carga_caldeira = producao_diaria * 1.075
    eficiencia_tss = (producao_diaria / 7700) * 100
    eficiencia_agua_evaporada = (capacidade_agua_evaporada / 1750) * 100

    # Exibir os resultados em colunas
    st.subheader("Resultados da análise de performance da Evaporação:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("💧 Capacidade de água evaporada", f"{capacidade_agua_evaporada:.0f} t/h")
        st.metric("🏭 Produção diária de licor virgem", f"{producao_diaria:.0f} tss/dia")
    with col2:
        st.metric("🔥 Carga da caldeira (com cinzas)", f"{carga_caldeira:.0f} tss/dia")
        st.metric("Eficiência de água evaporada", f"{eficiencia_agua_evaporada:.0f} %")
        st.metric("Eficiência de processamento de sólidos", f"{eficiencia_tss:.0f} %")
   
