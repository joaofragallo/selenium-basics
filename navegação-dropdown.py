from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
import time

opcoes = Options()
navegador = webdriver.Firefox(options=opcoes) 
time.sleep(3)
navegador.get("https://the-internet.herokuapp.com/dropdown")
navegador.maximize_window()
time.sleep(3) 
caixa = navegador.find_element(By.ID, "dropdown")
time.sleep(2)
menu = Select(caixa)
menu.select_by_visible_text("Option 2")
time.sleep(2)
navegador.quit()