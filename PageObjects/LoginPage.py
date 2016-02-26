from selenium.webdriver.common.by import By
from PageObjects.GenericPage import GenericPage
import os

__author__ = 'hcassus'


class LoginPage(GenericPage):

    locator_user = (By.ID, 'id_usuario')
    locator_password = (By.ID, 'id_senha')
    locator_access = (By.XPATH, '//button[text() = "ENTRAR"]')

    VALID_PASSWORD = os.environ.get('VALID_PASSWORD','')
    VALID_LOGIN = os.environ.get('VALID_LOGIN','')

    def preencher_usuario(self, user):
        user_element = self.driver.find_element(*LoginPage.locator_user)
        user_element.send_keys(user)

    def preencher_senha(self, password):
        password_element = self.driver.find_element(*LoginPage.locator_password)
        password_element.send_keys(password)

    def clicar_entrar(self):
        access_element = self.driver.find_element(*LoginPage.locator_access)
        access_element.click()





