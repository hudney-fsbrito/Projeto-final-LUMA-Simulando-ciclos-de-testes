from features.pages.base_page import wait_for_elements
from selenium.webdriver.common.by import By
from features.helpers.driver import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def clicar_menu_dropdown():
    wait = WebDriverWait(get_driver(), 10)
    menu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-action="customer-menu-toggle"]')))
    menu.click()

def clicar_my_account():
    wait = WebDriverWait(get_driver(), 10)
    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account")))
    link.click()

def clicar_address_book():
    wait = WebDriverWait(get_driver(), 10)
    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Address Book")))
    link.click()

def botao_novo_endereco():
    wait = WebDriverWait(get_driver(), 10)
    botao = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="Add New Address"]'))).click()

def preencher_endereco():
    wait_for_elements("#country").send_keys("Brazil")
    dropdown_element = wait_for_elements("#region_id")
    Select(dropdown_element).select_by_visible_text("Pernambuco")
    wait_for_elements("#zip").send_keys("50761060")
    wait_for_elements("#telephone").send_keys("81987552422")
    wait_for_elements("#street_1").send_keys("rua arsênio calaça") 
    wait_for_elements("#city").send_keys("Recife")

def clicar_botao_salvar():
    wait_for_elements("button.save.primary").click()

def mensagem_endereco_salvo():
    texto = wait_for_elements('div[data-bind="html: $parent.prepareMessageForHtml(message.text)"]').text
    assert texto == "You saved the address.", f"Mensagem não encontrada. Recebido: '{texto}'"