from behave import when
from PageObjects.HomePage import HomePage

__author__ = 'hcassus'

class HomePageSteps:

    @when('I click in "Fazer Login"')
    def click_login(self):
        HomePage.click_login(self)
