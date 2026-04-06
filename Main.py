import pandas as pd
import plotly.express as px


tabela = pd.read_csv("cancelamentos.csv")


tabela = tabela.drop(columns=["CustomerID"])


tabela = tabela.dropna()


print("Distribuição de cancelamentos:")
print(tabela["cancelou"].value_counts())
print("\nPercentual:")
print(tabela["cancelou"].value_counts(normalize=True))


for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    grafico.show()


tabela = tabela[tabela["duracao_contrato"] != "Monthly"]
tabela = tabela[tabela["ligacoes_callcenter"] <= 4]
tabela = tabela[tabela["dias_atraso"] <= 20]


print("\nApós aplicar filtros:")
print(tabela["cancelou"].value_counts())
print("\nPercentual:")
print(tabela["cancelou"].value_counts(normalize=True))
