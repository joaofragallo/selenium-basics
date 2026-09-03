from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

opcoes = Options()
navegador = webdriver.Firefox(options=opcoes) 
time.sleep(3)
navegador.get("https://the-internet.herokuapp.com/login")
navegador.maximize_window()
time.sleep(3) 
navegador.find_element(By.ID ,"username").send_keys("tomsmith", Keys.TAB)
navegador.find_element(By.ID ,"password").send_keys("SuperSecretPassword!", Keys.ENTER)
navegador.save_screenshot("tomsmith")
