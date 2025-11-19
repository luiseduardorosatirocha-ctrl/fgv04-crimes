import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Análise de Crimes - FGV Direito Rio")

# Upload do CSV
uploaded_file = st.file_uploader("Envie o arquivo CSV com os dados dos crimes", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Pré-visualização dos dados")
    st.write(df.head())

    # Gráfico de barras: crimes por tipo
    st.subheader("Crimes por Tipo")
    crime_tipo = df.groupby("tipo_crime")["numero_registros"].sum()

    fig1, ax1 = plt.subplots()
    ax1.bar(crime_tipo.index, crime_tipo.values)
    ax1.set_xlabel("Tipo de Crime")
    ax1.set_ylabel("Quantidade")
    ax1.set_title("Quantidade de Crimes por Tipo")
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    # Gráfico de linha: crimes por estado ao longo dos anos
    st.subheader("Crimes por Estado ao longo dos Anos")
    crimes_estado_ano = df.groupby(["estado", "ano"])["numero_registros"].sum().reset_index()

    fig2, ax2 = plt.subplots()
    for estado in crimes_estado_ano["estado"].unique():
        dados_estado = crimes_estado_ano[crimes_estado_ano["estado"] == estado]
        ax2.plot(dados_estado["ano"], dados_estado["numero_registros"], label=estado)

    ax2.set_xlabel("Ano")
    ax2.set_ylabel("Número de Registros")
    ax2.set_title("Crimes por Estado ao longo dos Anos")
    ax2.legend()
    st.pyplot(fig2)

    # Relatório simples de tendências
    st.subheader("Relatório Automático de Tendências")
    tendencia_total = df.groupby("ano")["numero_registros"].sum().diff().fillna(0)
    maior_alta = tendencia_total.idxmax()
    maior_queda = tendencia_total.idxmin()

    st.write(f"• Ano com maior aumento no total de crimes: **{maior_alta}**")
    st.write(f"• Ano com maior queda no total de crimes: **{maior_queda}**")
else:
    st.info("Envie um arquivo CSV para iniciar a análise.")
