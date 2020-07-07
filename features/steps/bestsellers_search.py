from selenium.common import exceptions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

BESTSELLERS_LINK_TABS = (By.XPATH, "//div[@id='zg_tabs']")
BESTSELLERS_LINK_ITEM = (By.CSS_SELECTOR, "a[href*='zg_bs_tab']")
BESTSELLERS_TEXT = (By.CSS_SELECTOR, "div#zg_banner_text")

#Locators from LANA:
TOP_LINKS = (By.CSS_SELECTOR, '#zg_tabs a')



@given('Open amazon BestSellers page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    context.driver.get('https://www.amazon.com/Best-Sellers/zgbs/ref=zg-bsms-tab')


@then('{expected_item_count} bestsellers menu items are present')
def verify_amount_of_items(context, expected_item_count):
    expected_item_count = int(expected_item_count)  # 5
    context.driver.wait.until(correct_menu_items_present(BESTSELLERS_LINK_ITEM, expected_item_count),
                              "Amount of items is incorrect")
    actual = len(context.driver.find_elements(*BESTSELLERS_LINK_ITEM))
    assert expected_item_count == actual, f'Expected {expected_item_count} items, but got {actual} items'


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

'''
@then('Verify each top link opens a new page')
def click_open_new_page(context):
    # list_of_links = context.driver.find_element_by_xpath("//div[@id='zg_tabs']") #WebElement
    list_of_links = context.driver.find_elements_by_css_selector("a[href*='zg_bs_tab']")  # list object
    array_of_links = []
    index = 0

    for link in list_of_links:
            link_info = link.get_attribute("href")
            print("link_info " + link_info )
            array_of_links.append(link_info)

    for link in list_of_links:
        url_link = array_of_links[index]
        context.driver.execute_script("window.open(arguments[0])", url_link)
        window_after = context.driver.window_handles[-1]
        context.driver.switch_to_window(window_after)
        # do something...
        assert url_link == array_of_links[index], f'Expected {array_of_links[index]} url address, but got {url_link} url address'
        context.driver.switch_to.default_content()
        index += 1

    #ToDo stale element = you try interact with not existing on this page element
    # you get element ids different for every time the page is refreshed

    '''


@then('Verify each top link opens a new page') #version from Lana
def click_open_new_page(context):

    #for x in range(len(top_links)):
    for x in range(5):

        link_to_click = context.driver.find_elements(*TOP_LINKS)[x]
        #link_text = link_to_click_text
        print("link_to_click = " + str(link_to_click))
        print("x = " + str(x))
        link_to_click.click()
        #new_text = context.driver.find_elements(*BESTSELLERS_TEXT).text
        #assert link_text in new_text, f'Expected {link_text} to be in {new_text}'
        #new_text = context.driver.find_element(*HEADER)
    
    
    
    
