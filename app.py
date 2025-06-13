
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("dados_coleta_centro.csv")

st.set_page_config(page_title="Dashboard Coleta Centro", layout="centered", page_icon="🚧")
st.markdown("""
    <style>
        body { background-color: #0f1117; color: #ffffff; }
        .stMetric { background-color: #1c1f26; border-radius: 10px; padding: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("♻️ Dashboard Interativo - Coleta de Resíduos (Centro)")
st.markdown("### Selecione o mês para visualizar os dados")

meses = df["Mes"].unique().tolist()
mes_selecionado = st.selectbox("Mês", meses)
dados_filtrados = df[df["Mes"] == mes_selecionado]

coleta_am = int(dados_filtrados["Coleta_AM"].values[0])
coleta_pm = int(dados_filtrados["Coleta_PM"].values[0])
total = int(dados_filtrados["Total"].values[0])

col1, col2, col3 = st.columns(3)
col1.metric("🌅 Manhã (kg)", f"{coleta_am:,}")
col2.metric("🌇 Tarde (kg)", f"{coleta_pm:,}")
col3.metric("📊 Total", f"{total:,}")

st.markdown("---")

data_bar = pd.DataFrame({
    "Período": ["Manhã", "Tarde"],
    "Quantidade": [coleta_am, coleta_pm]
})
fig_bar = px.bar(data_bar, x="Período", y="Quantidade", color="Período",
                 color_discrete_sequence=["#00b4d8", "#f77f00"],
                 title=f"Coleta em {mes_selecionado}", height=400)
st.plotly_chart(fig_bar, use_container_width=True)

fig_pie = px.pie(data_bar, names="Período", values="Quantidade",
                color_discrete_sequence=["#00b4d8", "#f77f00"], hole=0.4)
fig_pie.update_layout(showlegend=True)
st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")
st.caption("Desenvolvido por Análise de Dados - Projeto Zeladoria Centro ✨")
