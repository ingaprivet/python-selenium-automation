from pages.base_page import Page
from pages.top_nav_menu import TopNavMenu
from pages.search_results_page import SearchResults
from pages.cart_services import CartServices
from pages.sign_in_services import SignInServices
from pages.hamburger_menu_services import HamburgerMenuServices


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.page = Page(self.driver)
        self.top_nav_menu = TopNavMenu(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.cart_services = CartServices(self.driver)
        self.sign_in_services = SignInServices(self.driver)
        self.hamburger_menu_services = HamburgerMenuServices(self.driver)

