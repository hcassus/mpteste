from behave import given
from selenium import webdriver


class GenericSteps():

    @given('I access "{url}"')
    def access_url(self, url):
        self.driver.get(url)
