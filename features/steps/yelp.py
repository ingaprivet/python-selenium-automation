#class work
from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

'''Give Open a company's Yelp page
    When Click on a website link
    And Switch to a new window
    Then The company's website is open
    And A user can close the new window and go to the original one'''

WEBSITE_LINK = (By.XPATH, "//*[contains(text(), 'anchors-fish-chips-and-sea')]")
COMPANY_NAME = (By.XPATH, "//*[contains(text(), 'Anchors fish & chips and sea food grill')]")

@given ("Open a company's Yelp page")
def open_yelp(context):
    context.driver.get("https://www.yelp.com/biz/anchors-fish-and-chips-and-seafood-grill-san-jose-2")

@when ("Click on a website link")
def click_link(context):
    context.original_windows = context.driver.window_handles #will pass original_windows to context
    # to be used in next step!
    print(context.original_windows)
    context.original_window = context.driver.current_window_handle
    print(context.original_window)
    context.driver.find_element(*WEBSITE_LINK).click()

@when ("Switch to a new window")
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    print(current_windows)
    #context.driver.switch_to_window(current_windows[1])
    for old_window in context.original_windows:
        current_windows.remove(old_window)
    print(current_windows)
    context.driver.switch_to_window(current_windows[0])

@then("The {company} website is open")
def verify_website_name(context, company):
    context.driver.find_element(*COMPANY_NAME) #only look for the element?!
    assert context.driver.find_element(*COMPANY_NAME), f"Expexted to find {company} name on a page"

@then("A user can close the new window and go to the original one")
def close_window_and_go_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)







