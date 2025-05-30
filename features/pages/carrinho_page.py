import time
from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.support.ui import Select
# from features.pages.carrinho_page import BOTAO_ADD_TO_CART

#_________ BOTÕES _________

BOTAO_FAZER_CHECKOUT = "#top-cart-btn-checkout"
BOTAO_ADD_TO_CART = "#product-addtocart-button"
BOTAO_NEXT = "//button[@class='button action continue primary']"
BOTAO_PLACE_ORDER = "//button[@class='action primary checkout']"
BOTAO_CARRINHO_DE_COMPRAS = ".showcart"

#_________ CAMPO DE ESCOLHA DE PRODUTO _________
PRODUTO_ITEM = ".product-image-photo"
TAMANHO_DO_PRODUTO = "#option-label-size-143-item-168"
COR_DO_PRODUTO = "#option-label-color-93-item-56"
QUANTIDADE_DO_PRODUTO = "#qty"

#_________ CAMPO DE FORMULÁRIO DE ENDEREÇO _________

CAMPO_NOME_NO_CARRINHO = "#HLRRSBL"
CAMPO_SOBRENOME_NO_CARRINHO = "#DHH1CEE"
PAIS = "#UUY0WED"
ESTADO = "#VYF770S"
CIDADE = "#LNDWA0J"
CEP = "#HBFHTT6"
RUA= "#QP2ISQY"
TELEFONE= "#WMYSR4C"
FRETE_INTPUT = "//input[@value='flatrate_flatrate']"

#_________ CAMPO DA MENSAGEM DE VALIDAÇÃO _________
CAMPO_MESNSAGEM_DE_CONFIRMACAO = ".base"

quantidade = "1"
mensagem_compra_criada_sucesso = "Thank you for your purchase!"

#Método de click
def clica_add_to_cart():
    find_element(BOTAO_ADD_TO_CART).click()
    time.sleep(5)

def clica_no_carrinho():
    find_element(BOTAO_CARRINHO_DE_COMPRAS).click()

def fazer_checkout():
    find_element(BOTAO_FAZER_CHECKOUT).click()

def escolhe_frete():
    get_driver().find_element(By.XPATH, FRETE_INTPUT).click()

def clica_proximo():
    get_driver().find_element(By.XPATH, BOTAO_NEXT).click()
    time.sleep(5)

def clica_fazer_pedido():
    btn = get_driver().find_element(By.XPATH, BOTAO_PLACE_ORDER)
    time.sleep(5)
    btn.click()
    
    

# Métodos de seleção de produto
def seleciona_produto():
    find_element(PRODUTO_ITEM).click()

def seleciona_tamanho():
    find_element(TAMANHO_DO_PRODUTO).click()

def seleciona_cor():
    find_element(COR_DO_PRODUTO).click()

def edita_quantidade():
    find_element(QUANTIDADE_DO_PRODUTO).send_keys(quantidade)

def adicionar_produto_carrinho():
    seleciona_produto()
    seleciona_tamanho()
    seleciona_cor()
    edita_quantidade()
    clica_add_to_cart()

def finalizar_pedido():
    clica_no_carrinho()
    fazer_checkout()
    escolhe_frete()
    clica_proximo()
    clica_fazer_pedido()
    time.sleep(5)


# VALIDA COMPRA
def mensagem_de_pedido_efetuado():
    return find_element(CAMPO_MESNSAGEM_DE_CONFIRMACAO).text.strip()

def mensagem_esperada_de_compra():
    return mensagem_compra_criada_sucesso