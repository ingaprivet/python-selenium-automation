from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInServices(Page):
    ORDERS_LINK = (By.ID, 'nav-orders')
    SIGN_IN_TEXT = (By.CSS_SELECTOR, "h1.a-spacing-small")

    def click_orders_link(self):
        self.click(*self.ORDERS_LINK)

    def verify_found_results_text(self, search_text):
        empty_cart_text = self.find_element(*self.SIGN_IN_TEXT).text
        assert search_text in empty_cart_text, f'Incorrect header: {empty_cart_text}'
