
import streamlit as st
import pandas as pd
import datetime
from io import BytesIO

st.set_page_config(page_title="Comissão La Cor", layout="centered")

st.title("🧾 Calculadora de Comissão - La Cor Tintas")

# Lista de funcionários e dados pré-definidos
funcionarios = {
    "Lucas Alves dos Santos": {"categoria": "vendedor", "meta": 80000, "adiantamento": 1000, "salario": 5000, "dias_ferias": 12},
    "Ronaldo Ferreira do Carmo": {"categoria": "vendedor", "meta": 50000, "adiantamento": 800, "salario": 3000},
    "Bruno Cabral Fialho": {"categoria": "vendedor", "meta": 50000, "adiantamento": 680, "salario": 3000},
    "Emerson Almeida Martins": {"categoria": "vendedor", "meta": 50000, "adiantamento": 680, "salario": 3000},
    "Maritélia Souza C. Serra": {"categoria": "vendedor", "meta": 90000, "adiantamento": 787.5, "salario": 3000},
    "Eunice Sangi da Silva": {"categoria": "gerente", "meta": 0, "adiantamento": 2000, "salario": 5000},
}

with st.form("formulario"):
    nome = st.selectbox("Selecione o Funcionário", list(funcionarios.keys()))
    dados = funcionarios[nome]
    
    categoria = dados["categoria"]
    salario_base = dados["salario"]
    meta = st.number_input("Meta do Mês", value=dados.get("meta", 0.0), step=100.0)
    valor_recebido = st.number_input("Valor Recebido (caso aplicável)", min_value=0.0, step=100.0)
    adiantamento = st.number_input("Adiantamento Recebido", value=dados.get("adiantamento", 0.0), step=50.0)
    desconto = st.number_input("Descontos Diversos", min_value=0.0, step=50.0)
    dias_ferias = st.number_input("Dias de Férias (se houver)", value=dados.get("dias_ferias", 0), step=1)

    submitted = st.form_submit_button("Calcular e Gerar Relatório")

if submitted:
    perc_comissao = 0.03
    perc_bonus = 0.10
    perc_dsr = 1/6

    if valor_recebido:
        comissao = valor_recebido * perc_comissao
        bonus = comissao * perc_bonus if valor_recebido >= meta else 0
        dsr = (comissao + bonus) * perc_dsr
        comissao_liquida = comissao + bonus - dsr
    else:
        dias_uteis = 30 - dias_ferias
        comissao = (dias_uteis / 30) * salario_base * 0.5
        bonus = comissao * perc_bonus
        dsr = (comissao + bonus) * perc_dsr
        comissao_liquida = comissao + bonus - dsr

    complemento = max(0, salario_base - comissao_liquida)
    total_bruto = comissao_liquida + complemento
    total_liquido = total_bruto - adiantamento - desconto

    resultado = {
        'Nome': nome,
        'Categoria': categoria,
        'Valor Recebido': valor_recebido,
        'Meta': meta,
        'Comissão': round(comissao, 2),
        'Bônus': round(bonus, 2),
        'DSR': round(dsr, 2),
        'Comissão Líquida': round(comissao_liquida, 2),
        'Complemento': round(complemento, 2),
        'Total Bruto': round(total_bruto, 2),
        'Adiantamento': adiantamento,
        'Desconto': desconto,
        'Total Líquido': round(total_liquido, 2)
    }

    st.subheader("💰 Resultado da Comissão")
    st.json(resultado)

    df = pd.DataFrame([resultado])
    data_atual = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')
    arquivo_excel = f"Relatorio_Comissao_{nome}_{data_atual}.xlsx"
    
    output = BytesIO()
    df.to_excel(output, index=False, engine='openpyxl')
    st.download_button(
        label="📥 Baixar Excel do Relatório",
        data=output.getvalue(),
        file_name=arquivo_excel,
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
