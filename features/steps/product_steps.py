from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.app.product_page.open_product(product_id)


@when('Hover over Add To Cart button')
def hover_add_to_cart(context):
    context.app.product_page.hover_add_to_cart()


@when('Hover over New Arrivals link')
def hover_over_link(context):
    context.app.product_page.hover_over_link()


@then('Verify size selection tooltip is shown')
def verify_size_tooltip(context):
    context.app.product_page.verify_size_tooltip()


@then('Verify the deals are shown')
def verify_deals_shown(context):
    context.app.product_page.verify_deals_shown()
