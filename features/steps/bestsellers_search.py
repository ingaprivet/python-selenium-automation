from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BESTSELLERS_TEXT = (By.CSS_SELECTOR, "div#zg_banner_text")

@given('Open amazon BestSellers page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@when('Verify Zeitgeist menu is displayed')
def verify_found_results_text(context):
    bestsellers_text = context.driver.find_element(*BESTSELLERS_TEXT).text
    print("BESTSELLERS_TEXT displayed = {0}".format(bestsellers_text))
    assert 'Amazon Best Sellers' in bestsellers_text, f'Incorrect page is found: {bestsellers_text}'


@then("Verify 5 links")
def count_available_tabs(context):
    bestsellers_links = context.driver.find_elements(By.CSS_SELECTOR, "a[href*='zg_bs_tab']")

    if len(bestsellers_links) == 5:
        print("Length of elements = {0}".format(len(bestsellers_links)))
        print("Test is passed")
    elif len(bestsellers_links) < 5:
        print("Length of elements = {0}".format(len(bestsellers_links)))
        print("Test is not passed")
    sleep(1)
