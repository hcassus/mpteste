from behave import when
from PageObjects.LoginPage import LoginPage
import os

__author__ = 'hcassus'

class LoginPageSteps():

    VALID_PASSWORD = os.environ.get('VALID_PASSWORD', '')
    VALID_LOGIN = os.environ.get('VALID_LOGIN', '')

    @when('I log in with valid credentials')
    def perform_login(self):
        LoginPage.fill_in_user_field(self, self.VALID_LOGIN)
        LoginPage.fill_in_password_field(self, self.VALID_PASSWORD)
        LoginPage.click_enter_button(self)
