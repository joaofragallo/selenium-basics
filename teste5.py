from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import pandas as pd
import time

# 1. Lê a planilha do Excel usando o Pandas
tabela = pd.read_excel("clientes.xlsx")

# 2. Inicia o navegador
opcoes = Options()
navegador = webdriver.Firefox(options=opcoes)

# 3. Laço de repetição: Para cada linha dentro da tabela, faça o seguinte:
for index, linha in tabela.iterrows():
    
    # Pega os dados da linha atual usando o nome exato da coluna no Excel
    nome_atual = linha["nome"]
    email_atual = linha["email"]
    telefone_atual = linha["telefone"]
    
    # Acessa o site do formulário a cada repetição
    navegador.get("https://docs.google.com/forms/d/e/1FAIpQLSfnDvmd4dIhqqdio-Cwa1gEav7Fla-W_-fSGizPhL7zPG6P_A/viewform?usp=publish-editor")
    time.sleep(2) # Aguarda o formulário carregar
    
    # Preenche os campos
    navegador.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(nome_atual)
    navegador.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(email_atual)
    navegador.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(str(telefone_atual))
    
    # Clica no botão de enviar
    navegador.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span").click()
    
    print(f"Formulário preenchido para: {nome_atual}")
    time.sleep(2) # Pausa antes de ir para o próximo cliente

# Quando acabar todas as linhas da planilha, fecha o navegador
print("Todas as linhas foram processadas!")
navegador.quit()