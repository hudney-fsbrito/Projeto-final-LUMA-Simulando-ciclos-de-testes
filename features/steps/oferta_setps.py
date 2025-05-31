import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.login_page import *
from features.pages.oferta_page import clicar_sale, validar_clicar_sale
from features.steps.login_steps import acessar_site_LUMA


@given(u'que o usuário esteja na página home page')
def inicio_homepage(context):
    acessar_site_LUMA(context)
    


@when(u'clica no sale')
def clica_no_link_sale(context):
    clicar_sale()

    


@then(u'deve ser redirecionado para página sale')
def validar_sale(context):
    validar_clicar_sale()

    
    
