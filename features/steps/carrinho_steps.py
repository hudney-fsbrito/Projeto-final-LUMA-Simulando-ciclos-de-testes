import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.carrinho_page import (adicionar_produto_carrinho, finalizar_pedido,
    mensagem_de_pedido_efetuado, mensagem_esperada_de_compra)
from features.pages.login_page import *
from features.steps.login_steps import acessar_site_LUMA, clicar_sign_in, preencher_dados_login

@given(u'adicione o produto no carrinho')
def adicionar_produto(context):
    acessar_site_LUMA(context)
    clicar_sign_in(context)
    preencher_dados_login(context)

    adicionar_produto_carrinho()
    


@when(u'finaliza o processo de pedido')
def step_impl(context):
    finalizar_pedido()
    


@then(u'a mensagem Thank you for your purchase! deverá surgir')
def valida_compra(context):
    assert mensagem_de_pedido_efetuado() == mensagem_esperada_de_compra(), f"\nEsperados: {mensagem_esperada_de_compra()}\nRecebidos: {mensagem_de_pedido_efetuado()}"