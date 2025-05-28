from features.helpers.driver import get_driver
from features.pages.base_page import *

BOTAO_CLICK_ME = '#buttonSimple'
CAMPO_NOME = "#formNome"
    
def get_campo_nome():
    return find_element(CAMPO_NOME)

def clicar_botao_click_me():
    # Verificar o texto inicial do botão
    assert get_element_text(BOTAO_CLICK_ME) == "Clique Me!"
    # Clicar no botão
    find_element(BOTAO_CLICK_ME).click()

def recuperar_texto_botao_click_me():
    # Localizar o elemento do botão
    return get_element_text(BOTAO_CLICK_ME)
    
