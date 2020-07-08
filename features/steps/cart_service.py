#Homework 7
from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amaxon page')
def open_amazon(context):
    context.app.page.open_page()


@when('Click on Cart Icon')
def click_cart_icon(context):
    context.app.cart_services.click_cart_icon()


@then('Verify {search_text} text present')
def verify_found_results_text(context, search_text):
    context.app.cart_services.verify_found_results_text(search_text)
