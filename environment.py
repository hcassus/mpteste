from selenium import webdriver

__author__ = 'hcassus'

def before_all(context):
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

def after_all(context):
    context.driver.quit()