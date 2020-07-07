from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartServices(Page):
    CART_ID = (By.ID, 'nav-cart')
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty")

    def click_cart_icon(self):
        self.click(*self.CART_ID)

    def verify_found_results_text(self, search_text):
        empty_cart_text = self.find_element(*self.EMPTY_CART_TEXT).text
        assert search_text in empty_cart_text, f'Incorrect header: {empty_cart_text}'

