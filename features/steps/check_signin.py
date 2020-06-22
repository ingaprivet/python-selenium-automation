from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.ID, 'nav-orders')
SEARCH_SUBMIT = (By.XPATH, "//a[@id='nav-link-accountList']")

@given('Open Amazon page to check sign in')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')

@when('Click Orders open the Sign-in page')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)

