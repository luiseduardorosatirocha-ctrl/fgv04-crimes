# Aplicação de Análise de Crimes – FGV Direito Rio

Este repositório contém um aplicativo desenvolvido em **Python + Streamlit** para analisar dados criminais a partir da base disponibilizada em formato CSV.

---

## 🔗 URL do Repositório no GitHub
https://github.com/luiseduardorosatirocha-ctrl/fgv-crimes

---

## 🔗 Base de Dados Utilizada
Os dados foram obtidos a partir do seguinte dashboard no Power BI:

https://app.powerbi.com/view?r=eyJrIjoiYThmMDBkNTYtOGU0Zi00MjUxLWJiMzAtZjFlMmYzYTgwOTBlIiwidCI6ImViMDkwNDIwLTQ0NGMtNDNmNy05MWYyLTRiOGRhNmJmZThlMSJ9

A base foi exportada para **arquivo CSV**, que deve ser enviado pelo usuário no aplicativo.

---

## 📁 Estrutura esperada do CSV

O arquivo CSV utilizado **não precisa ter nomes exatos de colunas**, pois o aplicativo permite escolher manualmente as colunas que representam cada informação.

O CSV deve conter, no mínimo, campos equivalentes a:

- **Tipo de crime**
- **Estado (UF)**
- **Ano**
- **Número de registros**

Mesmo que os nomes estejam diferentes (ex.: “Categoria”, “UF”, “Ano do fato”, “Registros”), o Streamlit permitirá selecionar cada coluna manualmente.

---

## 🖥️ Funcionalidades do Aplicativo

O aplicativo gera automaticamente:

### ✔️ **1. Gráfico de Barras — Crimes por Tipo**
Mostra a soma total de registros para cada categoria de crime.

### ✔️ **2. Gráfico de Linhas — Crimes por Estado ao Longo dos Anos**
Cada linha representa um estado, exibindo a evolução ano a ano.

### ✔️ **3. Relatório Automático de Tendências**
Inclui:
- Ano com maior aumento de registros
- Ano com maior queda
- Linha temporal com o total anual de crimes

---

## ▶️ Como rodar o aplicativo localmente

1. Instale as dependências:
```bash
pip install -r requirements.txt
