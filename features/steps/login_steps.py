import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.login_page import *
# from features.steps.login_steps import acessar_site_treinamento

# Testa cadastro novo de conta com sucesso
@given(u'que a página de LUMA seja acessada e clicado em Create an Account')
def acessar_site_LUMA(context):
    get_driver().get("https://magento.softwaretestingboard.com/")


@when(u'o formulário Create New Customer Account for preechido')
def preencher_campos_criar_nova_conta(context):
    clicar_link_criar_conta()
    preencher_criar_conta()
    clicar_botao_criar_conta()


@then(u'a conta deve ser criada com sucesso')
def validar_conta_criada(context):
    # verificar_url_esperada()
    assert mensagem_recuperada_de_conta_criada() == mensagem_esperada_de_conta_criada(), f"\nEsperados: {mensagem_esperada_de_conta_criada()}\nRecebidos: {mensagem_recuperada_de_conta_criada()}"

# Testa o login com sucesso
@given(u'que o usuário tenha cadastro')
def clicar_sign_in(context):
    acessar_site_LUMA(context)
    clicar_link_sign_in()

@when(u'os dados de login forem preechidos')
def preencher_dados_login(context):
    preencher_campo_login()
    clicar_botao_login()

@then(u'o nome do usuário deve aparecer no topo da tela')
def validar_login_sucesso(context):
    print(f"Mensagem esperada: {mensagem_esperada_seja_bem_vindo()}")
    print(f"Mensagem recuperada: {mensagem_recuperada_seja_bem_vindo()}")
    assert mensagem_recuperada_seja_bem_vindo() == mensagem_esperada_seja_bem_vindo(), f"\nEsperados: {mensagem_esperada_seja_bem_vindo()}\nRecebidos: {mensagem_recuperada_seja_bem_vindo()}"
    