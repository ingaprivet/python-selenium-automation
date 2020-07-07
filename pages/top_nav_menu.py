from selenium.webdriver.common.by import By
from pages.base_page import Page


class TopNavMenu(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_SUBMIT = (By.XPATH, "//input[@value='Go']")

    def search_word(self, search_word):
        self.input(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_SUBMIT)
