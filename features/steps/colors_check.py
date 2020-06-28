from behave import when, then, given
from selenium.webdriver.common.by import By

COLOR_TOGGLE_GROUP = (By.ID, "variation_color_name")
COLOR_SELECTION_NAMES = (By.XPATH, "//li[starts-with(@id,'color_name_')]")


@given('Open a Product page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')


@when('Color selection toggle group is available')
def verify_found_results_text(context):
    color_toggle_group = context.driver.find_element(*COLOR_TOGGLE_GROUP).text
    assert "Color:" in color_toggle_group, "Expected word Color: in message, but got '{}'".format(color_toggle_group)


@then('{expected_item_count} color choices items are present')
def verify_amount_of_items(context, expected_item_count):
    expected_item_count = int(expected_item_count)  # 8
    context.driver.wait.until(correct_menu_items_present(COLOR_SELECTION_NAMES, expected_item_count),
                              "Amount of items is incorrect")
    actual = len(context.driver.find_elements(*COLOR_SELECTION_NAMES))
    assert expected_item_count == actual, f'Expected {expected_item_count} items, but got {actual} items'


@then('Loop thru available colors')
def verify_list_of_colors(context):
    counter = 0
    color_elements = context.driver.find_elements(*COLOR_SELECTION_NAMES)
    for el in color_elements:
        el.click()
        counter += 1
    print(f'Looped thru the list of color ' + str(counter) + ' times')


class correct_menu_items_present(object):

    def __init__(self, locator, amount):
        self.locator = locator
        self.amount = amount

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)  # Finding the referenced element
        if len(elements) == self.amount:
            return elements
        else:
            return False
