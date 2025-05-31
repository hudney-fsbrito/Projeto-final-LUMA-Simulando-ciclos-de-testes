from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.support.ui import Select

LINK_SALE = '//a[@href="https://magento.softwaretestingboard.com/sale.html"]'
url_esperada = "https://magento.softwaretestingboard.com/sale.html"

def clicar_sale():
    get_driver().find_element(By.XPATH,LINK_SALE).click()



def validar_clicar_sale():
    verificar_url_esperada(url_esperada)

def verificar_url_esperada(url_esperada):
    url_atual = get_driver().current_url
    assert url_atual == url_esperada, f"Erro: Esperado a URL '{url_esperada}', mas obtido '{url_atual}'"
    print("A URL está correta.")