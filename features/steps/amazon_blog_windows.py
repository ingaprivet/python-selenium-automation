from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

AMAZON_BLOG_LINK = (By.XPATH, "//*[text()[contains(.,'See daily updates at blog.aboutamazon.com')]]")
AMAZON_BLOG_PAGE_TEXT = (By.XPATH, "//*[text()[contains(.,'Company news')]]")


@when('Store original windows')
def store_window_info(context):
    context.original_windows = context.driver.window_handles  # will pass original_windows to context
    # to be used in next step!
    context.original_window = context.driver.current_window_handle

@when('Click on blog link “See daily updates at blog.aboutamazon.com”')
def click_amazon_blog_link(context):
    #context.driver.wait.until(EC.presence_of_element_located(AMAZON_BLOG_LINK)).click()
    context.driver.find_element(*AMAZON_BLOG_LINK).click()


@when('Switch to the newly opened window')
def verify_switched_to_child_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    # context.driver.switch_to_window(current_windows[1])
    for old_window in context.original_windows:
        current_windows.remove(old_window)
    context.driver.switch_to_window(current_windows[0])

@then('Amazon Blog is opened')
def verify_blog_window_is_opened(context):
        context.driver.find_element(*AMAZON_BLOG_PAGE_TEXT)  # only look for the element?!
        assert context.driver.find_element(*AMAZON_BLOG_PAGE_TEXT), f"Expected to find Company news on a page"


@then('User can open and close Blog menu')
def close_window_and_go_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)


