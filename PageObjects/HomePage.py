from selenium.webdriver.common.by import By
from PageObjects.GenericPage import GenericPage

__author__ = 'hcassus'


class HomePage(GenericPage):

    login_locator = (By.LINK_TEXT,'Fazer login')

    def click_login(self):
        login_element = self.driver.find_element(*HomePage.login_locator)
        login_element.click()
