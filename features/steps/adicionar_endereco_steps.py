from behave import given, when, then
from features.pages.login_page import *
from features.pages.adicionar_endereco_page import *
from features.helpers.driver import get_driver
from features.steps.login_steps import *

@given(u'que o usuário esteja logado')
def esteja_logado(context):
    acessar_site_LUMA(context)
    clicar_sign_in(context)
    preencher_dados_login(context)

@when(u'clicar no menu de usuário')
def menu_usuario(context):
    clicar_menu_dropdown()


@when(u'clicar em "My Account"')
def my_account(context):
    clicar_my_account()


@when(u'clicar em "Address Book"')
def adress_book(context):
    clicar_address_book()


@when(u'clicar em "Adicionar novo endereço"')
def novo_endereco(context):
    botao_novo_endereco()


@when(u'preencher os dados obrigatórios')
def dados(context):
    preencher_endereco()


@when(u'clicar em "Salvar endereço"')
def salvar(context):
    clicar_botao_salvar()


@then(u'aparecer a mensagem "Você salvou o endereço."')
def mensagem(context):
    mensagem_endereco_salvo()