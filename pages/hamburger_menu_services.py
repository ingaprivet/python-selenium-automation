from selenium.webdriver.common.by import By
from pages.base_page import Page


class HamburgerMenuServices(Page):
    HAM_MENU = (By.ID, 'nav-hamburger-menu')
    AMAZON_MUSIC_MENU_ITEM = (
        By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
    AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")


    def click_ham_icon(self):
        self.click(*self.HAM_MENU)

    def click_amazon_music_icon(self):
        self.wait_for_element_click(*self.AMAZON_MUSIC_MENU_ITEM)

    def verify_amount_of_items(self, expected_item_count_str):
        expected_item_count = int(expected_item_count_str)  # 6
        self.driver.wait.until(correct_menu_items_present
                               (self.AMAZON_MUSIC_MENU_ITEM_RESULTS, expected_item_count),
                               "Amount of items is incorrect")
        actual = len(self.driver.find_elements(By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)"))
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
