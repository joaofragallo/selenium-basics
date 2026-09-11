from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import pandas as pd
import time
tabela = pd.read_excel("clientesfalsos.xlsx")
opcoes = Options()
navegador = webdriver.Firefox(options=opcoes)
for index, linha in tabela.iterrows():
    
    nome_atual = linha["Nome"]
    email_atual = linha["Email"]
    telefone_atual = linha["Telefone"]
  
    
    navegador.get("https://docs.google.com/forms/d/e/1FAIpQLSfnDvmd4dIhqqdio-Cwa1gEav7Fla-W_-fSGizPhL7zPG6P_A/viewform?usp=header")
    time.sleep(2) 

    navegador.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(nome_atual)
    navegador.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(email_atual)
    navegador.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(str(telefone_atual))
    navegador.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span").click()
    time.sleep(1)
    
    print(f"Formulário preenchido para: {nome_atual}")
    time.sleep(1) 

print("Todas as linhas foram processadas!")
navegador.quit()