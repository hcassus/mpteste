from behave import then
from PageObjects.MainPage import MainPage

__author__ = 'hcassus'


class MainSteps():

    @then('I check I am logged in as "{user}"')
    def verificar_usuario(self, user):
        assert MainPage.obter_usuario(self) == user
