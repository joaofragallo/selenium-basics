from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

opcoes = Options()
navegador = webdriver.Firefox(options=opcoes) 
time.sleep(3)
navegador.get("https://workspace.google.com/intl/pt-BR/gmail/")
navegador.maximize_window()
time.sleep(3) 
navegador.find_element(By.LINK_TEXT, "Fazer login").click()
abas = navegador.window_handles
navegador.switch_to.window(abas[1])
time.sleep(2)
navegador.find_element(By.ID, 'identifierId').send_keys("joao.fragallof@gmail.com", Keys.ENTER)
