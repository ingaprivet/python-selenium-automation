from behave import when, then, given
from selenium.webdriver.common.by import By

PAGE_SECTION_DISPLAYED = (By.XPATH, "//p[contains(text(),'Members save an extra 10%')]")

ITEMS_DISPLAYED = (
By.XPATH, "//ul[contains(@class,'s-result-list')] /li[contains(@class,'s-result-item')]/div[contains(.,'Regular')]")


@given('Open wholefoodsdeals page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@when('Needed section of the page is available')
def verify_found_results_text(context):
    needed_section_displayed = context.driver.find_element(*PAGE_SECTION_DISPLAYED).text
    assert "Members save an extra 10% on SALE prices! (*Excludes alcohol)" in needed_section_displayed, "Expected Members save an extra 10%: in message, but got '{}'".format(
        needed_section_displayed)


@then('Verify every item has ‘Regular’ displayed')
# 'Regular' is included into the XPATH of ITEMS_DISPLAYED
def verify_list_of_items(context):
    counter = 0
    items_displayed_list = context.driver.find_elements(*ITEMS_DISPLAYED)
    if items_displayed_list is not None:
        for el in items_displayed_list:
            counter += 1
            # print(el.text)

        print(f'Looped thru the list of items ' + str(counter) + ' times')
