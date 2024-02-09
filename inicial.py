# passo a passo do projeto
# passo 1: Importat a base de dados
import pandas as pd

tabela = pd.read_csv("cancelamentos_sample.csv")

# passo 2: visualizar a base de dados

tabela = tabela.drop(columns="CustomerID")
print(tabela)

# colunas inuteis - informações que não te ajudam, te atrapalham
# passo 3: corrigir as cagadas da base de dados
# valores vazios - esvaziar as linhas que tem valores vazios
print(tabela.info())
tabela = tabela.dropna()
print(tabela.info())
# passo 4: análise inicial dos cancelamentos

print(tabela["cancelou"].value_counts())
# em porcentual
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))
print(tabela["duracao_contrato"].value_counts(normalize=True))
print(tabela["duracao_contrato"].value_counts())
# passo 5: Analise das causa dos cancelamentos (como as colunas da base impactam no cacelamento)
# gráficos/dashboards
import plotly.express as px

# criar o grafico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    # exibir o grafico
    grafico.show()
    # clientes do contrato mensa todos cancelam
    # oferecer desconto nos planos anuais e trimestrais
# clientes que ligam mais do que 4 vezes para o call center, cancelam
    # criar um processo para resolver o problema do cliente em no maximo 3 ligações
# clientes com atrasaram mais de 20 dias, cancelaram
    # política d resolver  atrasos em até 10 dias (equipe financeiro)

tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
tabela = tabela[tabela["ligacoes_callcenter"]<=4]
tabela = tabela[tabela["dias_atraso"]<=20]

print(tabela["cancelou"].value_counts())
# em porcentual
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))