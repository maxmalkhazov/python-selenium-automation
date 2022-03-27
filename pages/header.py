from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from selenium.webdriver.support.ui import Select


class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-button')
    CART_COUNT = (By.ID, 'nav-cart-count')
    FLAG = (By.CSS_SELECTOR, '.icp-nav-flag')
    SPANISH_LANG = (By.CSS_SELECTOR, '[href="#switch-lang=es_US"]')
    SELECT_DEPARTMENT = (By.ID, 'searchDropdownBox')
    DEPARTMENT = (By.ID, 'nav-search-label-id')

    def search_product(self):
        self.input_text('coffee', *self.SEARCH_INPUT)

    def click_search(self):
        self.click(*self.SEARCH_BUTTON)

    def click_signin_popup(self):
        self.wait_for_element_appear(*self.SIGN_IN_POPUP_BTN).click()

    def verify_empty_cart(self):
        self.verify_text('0', *self.CART_COUNT)

    def hover_lang_options(self):
        flag = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(flag)
        actions.perform()

    def verify_spanish_lang_present(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def select_department(self, alias: str):
        select_department = self.find_element(*self.SELECT_DEPARTMENT)
        select = Select(select_department)
        select.select_by_value(f'search-alias={alias}')


