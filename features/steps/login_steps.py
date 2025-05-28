import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.login_page import *

@given(u'que a página de treinamento seja acessada')
def acessar_site_treinamento(context):
    get_driver().get("https://wcaquino.me/cypress/componentes.html")

@when(u'o botão click me for pressionado')
def press_botao_click_me(context):
    clicar_botao_click_me()

@then(u'o seu valor deverá mudar para "{texto_correto}"')
def verificar_alteracao_valor(context, texto_correto):
    valor_botao_teste = recuperar_texto_botao_click_me()
    assert valor_botao_teste == texto_correto, f"O texto obtido: {valor_botao_teste}\nDiferente do esperado: {texto_correto}"

@when(u'o valor "{nome}" for inserido no campo nome')
def inserir_valor_campo(context, nome):
    get_campo_nome().send_keys(nome)
    time.sleep(4)