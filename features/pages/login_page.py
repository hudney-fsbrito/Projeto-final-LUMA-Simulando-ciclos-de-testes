from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.support.ui import Select
# from features.steps.login_steps import preencher_campos, preencher_campos_criar_conta

# _____________ MAPEANDO CAMPO NA TELA _____________

# mapeando link
LINK_CRIAR_CONTA = "//a[@href='https://magento.softwaretestingboard.com/customer/account/create/']"
LINK_SIGN_IN = "//li[@class='authorization-link']"

# mapeando campos
CAMPO_NOME = "#firstname"
CAMPO_SOBRENOME = "#lastname"
CAMPO_EMAIL = "#email_address"
CAMPO_SENHA = "#password"
BOTAO_LOGIN_OK = "#send2"
CAMPO_CONFIRMA_SENHA = "#password-confirmation"
BOTAO_CRIAR_CONTA = "//button[@class='action submit primary']"
CAMPO_CONTA_CRIADA_SUCESSO = "//div[contains(@class, 'message-success')]//div"
CAMPO_SEJA_BEM_VINDO = ".logged-in"

# campos login
CAMPO_EMAIL_LOGIN = "#email"
CAMPO_SENHA_LOGIN = "#pass"

# campos para veirificação

# variáveis para teste
# url_esperada = "https://magento.softwaretestingboard.com/customer/account/"
mensagem_seja_bem_vindo = "Welcome," #Welcome, Marsupilame Bertoudo!
mensagem_conta_criada_sucesso = "Thank you for registering with Main Website Store."
nome = "Marsupilame"
sobrenome = "Bertoudo"
email = "marsuBE@gmail.com"
senha = "@MarsuBer1234"

# ___________________ MÉTODOS DE PREECHIMENTO DE CAMPO ___________________

def preencher_email_login():
    find_element(CAMPO_EMAIL_LOGIN).send_keys(email)

def preencher_senha_login():
    find_element(CAMPO_SENHA_LOGIN).send_keys(senha)
    
def preencher_nome():
    find_element(CAMPO_NOME).send_keys(nome)

def preencher_sobrenome_nome():
    find_element(CAMPO_SOBRENOME).send_keys(sobrenome)

def preencher_email():
    find_element(CAMPO_EMAIL).send_keys(email)

def preencher_senha():
    find_element(CAMPO_SENHA).send_keys(senha)

def preencher_confirma_senha():
    find_element(CAMPO_CONFIRMA_SENHA).send_keys(senha)


# ____________ MÉTODO CLICK ____________
    
def clicar_botao_login():
    # Localiza o link/botão para abrirpágina de criar conta
    find_element(BOTAO_LOGIN_OK).click()

def clicar_link_criar_conta():
    # Localiza o link/botão para abrirpágina de criar conta
    get_driver().find_element(By.XPATH, LINK_CRIAR_CONTA).click()

def clicar_link_sign_in():
    # Localiza o link/botão para abrir página de login
    get_driver().find_element(By.XPATH, LINK_SIGN_IN).click()

    # Clica no botão para criar conta
def clicar_botao_criar_conta():
    get_driver().find_element(By.XPATH, BOTAO_CRIAR_CONTA).click()

# ____________ MÉTODO PREENCHE FORMULÁRIO ____________
def preencher_campo_login():
    preencher_email_login()
    preencher_senha_login()

def preencher_criar_conta():
    preencher_nome()
    preencher_sobrenome_nome()
    preencher_email()
    preencher_senha()
    preencher_confirma_senha()


# ___________________ RECUPERAR VALORES ___________________

# Valida redirecionamento
# def verificar_url_esperada(url_esperada):
#     url_atual = get_driver().current_url
#     assert url_atual == url_esperada, f"Erro: Esperado a URL '{url_esperada}', mas obtido '{url_atual}'"
#     print("A URL está correta.")

def mensagem_recuperada_seja_bem_vindo():
    return find_element(CAMPO_SEJA_BEM_VINDO).text

def mensagem_esperada_seja_bem_vindo():
    return f"{mensagem_seja_bem_vindo} {nome} {sobrenome}!" #Welcome, Marsupilame Bertoudo!

def mensagem_recuperada_de_conta_criada():
    return get_driver().find_element(By.XPATH, CAMPO_CONTA_CRIADA_SUCESSO).text.strip()

def mensagem_esperada_de_conta_criada():
    return mensagem_conta_criada_sucesso