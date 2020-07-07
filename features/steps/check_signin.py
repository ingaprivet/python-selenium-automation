from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Click Orders')
def click_search_icon(context):
    context.app.sign_in_services.click_orders_link()


@then('Verify {search_text} page is opened')
def verify_found_results_text(context, search_text):
    context.app.sign_in_services.verify_found_results_text(search_text)
