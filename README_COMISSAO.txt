
# Aplicativo de Cálculo de Comissão - La Cor Tintas

## Linguagem Utilizada:
- Python 3
- Framework: Streamlit (aplicação Web)
- Bibliotecas: pandas, datetime

## Objetivo:
Permitir que colaboradores (como a Nice) preencham os dados do mês e gerem automaticamente um relatório de comissão em Excel, de forma visual, sem necessidade de programação.

## Como usar:

1. Crie uma conta gratuita em: https://share.streamlit.io
2. Crie um repositório no GitHub (ex: `comissao-lacor`)
3. Faça upload do arquivo `app_comissao_streamlit.py` neste repositório
4. No site do Streamlit, clique em **New app** e selecione o repositório e o arquivo
5. Clique em Deploy. Pronto! Seu app está no ar.

## Campos do sistema:
- Nome do Funcionário
- Categoria (vendedor, entregador ou gerente)
- Valor Recebido
- Meta do Mês
- Adiantamento
- Desconto
- Dias de Férias (se aplicável)

## Resultado:
- Calcula Comissão (3%)
- Bônus (10% se bater a meta)
- DSR proporcional (1/6)
- Complemento até salário mínimo garantido
- Total líquido a pagar
- Gera planilha Excel com um clique

Desenvolvido para facilitar o processo de conferência e fechamento da folha mensal.
