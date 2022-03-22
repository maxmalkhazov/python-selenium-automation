from selenium.webdriver.common.by import By

from pages.base_page import Page


class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')

    def search_product(self):
        self.input_text('coffee', *self.SEARCH_INPUT)

    def click_search(self):
        self.click(*self.SEARCH_BUTTON)