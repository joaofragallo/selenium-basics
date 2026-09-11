import pandas as pd
from faker import Faker

gerador = Faker('pt_BR')

dados = []

for _ in range(50):
    dados.append({
        "Nome": gerador.name(),          
        "Email": gerador.email(),        
        "Telefone": gerador.cellphone_number()  
    })
tabela = pd.DataFrame(dados)
tabela.to_excel("clientesfalsos.xlsx", index=False)
print("Planilha criada com sucesso! Verifique a sua pasta.")