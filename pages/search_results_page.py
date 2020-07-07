from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResults(Page):
    RESULTS_FOUND_MESSAGE = (By.CSS_SELECTOR, ".a-color-state.a-text-bold")

    def verify_found_results_text(self, search_world):
        print("in verify of SearchResults")
        search_result_header = self.find_element(*self.RESULTS_FOUND_MESSAGE).text
        assert search_world in search_result_header, f'Incorrect header: {search_result_header}'





