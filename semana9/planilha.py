import pandas as pd
from main import cadastrar

plan = pd.read_excel("Dados.xlsx")
print(plan)

for index, linha in plan.iterrows():
    cadastrar(linha['Atleta'], linha['Modalidade'], linha['Medalha'], linha['Comitê'])
    

    
