from selenium.webdriver.common.by import By
from PageObjects.GenericPage import GenericPage

__author__ = 'hcassus'


class MainPage(GenericPage):

    locator_logged_user = (By.ID, 'profile-text')

    def obter_usuario(self):
        elemento_user = self.driver.find_element(*MainPage.locator_logged_user)
        return elemento_user.text
