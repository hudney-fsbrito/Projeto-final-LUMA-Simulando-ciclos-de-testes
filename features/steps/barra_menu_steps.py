
from behave import given, then
from features.pages.login_page import *
from features.pages.barra_menu_page import menu_women_
from features.steps.login_steps import acessar_site_LUMA

@given(u'que o usuário está na página inicial')
def esta_na_pagina_inicial(context):
    acessar_site_LUMA(context)


@then(u'ele clica sobre o menu "Women" e abre a pagina "Women"')
def menu_women(context):
    menu_women_()
    
