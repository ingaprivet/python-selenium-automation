from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By

PRODUCT_OF_CHOICE = (By.XPATH, "//img[@alt='Echo Dot (3rd Gen) - Smart speaker with clock and Alexa - Sandstone']")
CART_NOT_EMPTY_TEXT = (By.XPATH, "//span[contains(text(),'(1 item):')]")


@given('Open a page with multiple Products')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/s?k=echo+dot&ref=nb_sb_noss_2')


@when('Click on Product image to add to Cart')
def click_search_icon(context):
    context.driver.find_element(*PRODUCT_OF_CHOICE).click()
    sleep(4)


@then('Verify a card is not empty')
def verify_found_results_text(context):
    search_result_header = context.driver.find_element(*CART_NOT_EMPTY_TEXT).text
    assert 'Your Amazon Cart is not empty' in search_result_header, f'Incorrect page is found: {search_result_header}'
