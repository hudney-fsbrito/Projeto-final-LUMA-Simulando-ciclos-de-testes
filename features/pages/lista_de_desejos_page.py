import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.login_page import *

CAMPO_ITEM_PRODUTO = ".product-image-photo"
BOTAO_LISTA_DESEJO = ".towishlist"
MENSAGEM_ADICIONADO_LISTA_DESEJO = "//div[contains(@class, 'message-success')]//div"
mensagem_sucesso_item_adicionado_desejo = "Radiant Tee has been added to your Wish List. Click here to continue shopping."

def clicar_no_produto():
    find_element(CAMPO_ITEM_PRODUTO).click()

def clicar_icone_desejo():
    find_element(BOTAO_LISTA_DESEJO).click()

def mensagem_recuperada():
    return get_driver().find_element(By.XPATH, MENSAGEM_ADICIONADO_LISTA_DESEJO).text.strip()

def mensagem_esperada_de_produto_adicionado_desejo():
    return mensagem_sucesso_item_adicionado_desejo







