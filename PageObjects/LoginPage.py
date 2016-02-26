from selenium.webdriver.common.by import By
from PageObjects.GenericPage import GenericPage
import os

__author__ = 'hcassus'


class LoginPage(GenericPage):

    user_locator = (By.ID, 'id_usuario')
    password_locator = (By.ID, 'id_senha')
    access_locator = (By.XPATH, '//button[text() = "ENTRAR"]')

    VALID_PASSWORD = os.environ.get('VALID_PASSWORD','')
    VALID_LOGIN = os.environ.get('VALID_LOGIN','')

    def fill_in_user_field(self, user):
        user_element = self.driver.find_element(*LoginPage.user_locator)
        user_element.send_keys(user)

    def fill_in_password_field(self, password):
        password_element = self.driver.find_element(*LoginPage.password_locator)
        password_element.send_keys(password)

    def click_enter_button(self):
        access_element = self.driver.find_element(*LoginPage.access_locator)
        access_element.click()





