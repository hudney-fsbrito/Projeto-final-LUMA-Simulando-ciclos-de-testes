from features.helpers.driver import get_driver
from features.pages.base_page import *


MENU_WOMEN = "//a[@href='https://magento.softwaretestingboard.com/women.html']"


def menu_women_():
    get_driver().find_element(By.XPATH, MENU_WOMEN).click()
    




