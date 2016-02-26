from selenium.webdriver.common.by import By
from PageObjects.GenericPage import GenericPage

__author__ = 'hcassus'


class MainPage(GenericPage):

    locator_logged_user = (By.ID, 'profile-text')
    locator_avatar = (By.CLASS_NAME, 'foto-do-usuario')

    def obtain_user(self):
        avatar_element = self.driver.find_element(*self.locator_avatar)
        avatar_element.click()

        user_element = self.driver.find_element(*self.locator_logged_user)
        return user_element.text
