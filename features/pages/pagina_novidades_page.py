from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.support.ui import Select
import time

#___ BUSCA DE ELEMENTO ___
LOGO_HOME = ".logo"
LINK_WHATS_NEW = "//a[@href='https://magento.softwaretestingboard.com/what-is-new.html']" 

#___ VARIÁVEL PARA AJUDAR TESTE ___
url_esperada = "https://magento.softwaretestingboard.com/what-is-new.html"



def volta_para_home():
    find_element(LOGO_HOME).click()

def verificar_url_esperada(url_esperada):
    time.sleep(5)
    url_atual = get_driver().current_url
    if url_atual == url_esperada:
        print("Não era essa não. Volta para home")
        volta_para_home()
    print("Url diferente")

def verifica_url_para_validacao(url_esperada):
    time.sleep(5)
    url_atual = get_driver().current_url
    assert url_atual == url_esperada, f"Erro: Esperado a URL '{url_esperada}', mas obtido '{url_atual}'"
    print("Validado!")

def valida_url():
    verifica_url_para_validacao(url_esperada)

def redireciona_homepage():
    verificar_url_esperada(url_esperada)

def clica_no_link_whats_new():
    # wait_for_element(5)
    get_driver().find_element(By.XPATH, LINK_WHATS_NEW).click()