import pandas as pd
from main import cadastrar

plan = pd.read_excel("PlanilhaLancamento.xlsx")

plan = plan.loc[plan['Nome'] == 'MARIANA MARCíLIO DE CARVALHO']
print(plan)

for index, linha in plan.iterrows():
    cadastrar(linha['Nome'], linha['Atividade'], linha['Nota'])