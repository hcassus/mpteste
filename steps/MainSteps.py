from behave import then
from PageObjects.MainPage import MainPage

__author__ = 'hcassus'


class MainSteps():

    @then('I check I am logged in as "{user}"')
    def verify_logged_user(self, user):
        assert MainPage.obtain_user(self) == user
