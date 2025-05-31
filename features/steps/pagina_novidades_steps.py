import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.login_page import *
from features.pages.pagina_novidades_page import clica_no_link_whats_new, redireciona_homepage, valida_url
from features.steps.login_steps import acessar_site_LUMA

@given(u'que o usuário esteja em uma página diferente da Whats New')
def homepage(context):
    acessar_site_LUMA(context)
    redireciona_homepage()
    
@when(u'clica no link What\'s New')
def entra_na_página_whats_new(context):
    clica_no_link_whats_new()


@then(u'deve ser redirecionado para página da What\'s New')
def valida_url_da_pagina(context):
    valida_url()