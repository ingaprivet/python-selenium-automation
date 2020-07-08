#By IngaB
from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.app.page.open_page()

@when('Search for {search_word}')
def input_search(context, search_word):
    context.app.top_nav_menu.search_word(search_word)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    context.app.search_results_page.verify_found_results_text(search_word)

