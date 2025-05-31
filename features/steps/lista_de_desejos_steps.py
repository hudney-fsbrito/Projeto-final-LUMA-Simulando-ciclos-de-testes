import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.lista_de_desejos_page import clicar_icone_desejo, clicar_no_produto, mensagem_esperada_de_produto_adicionado_desejo, mensagem_recuperada
from features.pages.login_page import *
from features.steps.login_steps import acessar_site_LUMA, clicar_sign_in, preencher_dados_login

@given(u'que o usuário clicou no item')
def clicar_no_item_de_produto(context):
    acessar_site_LUMA(context)
    clicar_sign_in(context)
    preencher_dados_login(context)
    clicar_no_produto()

@when(u'ele clica em "add to wish list"')
def clicar_botao_desejo(context):
    clicar_icone_desejo()

@then(u'o item vai para a "my wish list"')
def item_adicionado_lista_desejo(context):
    assert mensagem_recuperada() == mensagem_esperada_de_produto_adicionado_desejo(), f"\nEsperados: {mensagem_esperada_de_produto_adicionado_desejo()}\nRecebidos: {mensagem_recuperada()}"