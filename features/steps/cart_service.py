from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By

SHOPPING_CART_ICON = (By.ID, 'nav-cart')
EMPTY_CART_TEXT = (By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Click on Cart Icon')
def click_search_icon(context):
    context.driver.find_element(*SHOPPING_CART_ICON).click()
    sleep(4)


@then('Verify the Shopping Cart is empty')
def verify_found_results_text(context):
    search_result_header = context.driver.find_element(*EMPTY_CART_TEXT).text
    assert 'Your Amazon Cart is empty' in search_result_header, f'Incorrect page is found: {search_result_header}'
