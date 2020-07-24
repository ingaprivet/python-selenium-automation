from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select


class TopNavMenu(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_SUBMIT = (By.XPATH, "//input[@value='Go']")
    SELECT_DEPARTMENT = (By.CSS_SELECTOR, 'select.nav-search-dropdown')
    DISPLAYED_DEPARTMENT = (By.CSS_SELECTOR, 'div#nav-subnav a.nav-b')

    def search_word(self, search_word):
        self.input(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_SUBMIT)

    def select_department(self, alias):
        dep_selection_element = self.find_element(*self.SELECT_DEPARTMENT)
        select = Select(dep_selection_element)  # by select tag!!!
        select.select_by_value(f'search-alias={alias}')

    def verify_selected_department(self, selected_dep):
        self.verify_text(selected_dep, *self.DISPLAYED_DEPARTMENT)
