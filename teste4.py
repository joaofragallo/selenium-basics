from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
import time

opcoes = Options()
navegador = webdriver.Firefox(options=opcoes) 
time.sleep(3)
navegador.get("https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal")
time.sleep(3)
navegador.maximize_window()
time.sleep(3)
navegador.find_element(By.NAME, "search").send_keys("Curitiba", Keys.ENTER)
time.sleep(3)
resumo = navegador.find_element(By.XPATH, '//*[@id="mwQg"]').text
time.sleep(3)
print(f"O texto selecionado foi\n '{resumo}'")
navegador.quit()