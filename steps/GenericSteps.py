from behave import given
from selenium import webdriver


class GenericSteps():

    @given('I access "{url}"')
    def acess_url(self, url):
        self.driver.get(url)
