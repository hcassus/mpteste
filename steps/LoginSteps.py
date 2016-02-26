from behave import when
from PageObjects.LoginPage import LoginPage

__author__ = 'hcassus'

class LoginPageSteps():

    @when('I log in with valid credentials')
    def efetuar_login(self):
        LoginPage.preencher_usuario(self, LoginPage.VALID_LOGIN)
        LoginPage.preencher_senha(self, LoginPage.VALID_PASSWORD)
        LoginPage.clicar_entrar(self)
