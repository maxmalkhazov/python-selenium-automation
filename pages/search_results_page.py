
from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
    DEPARTMENT = (By.CSS_SELECTOR, '#nav-subnav[data-category="{DEPARTMENT_CATEGORY}"]')

    def get_department_locator(self, department: str):
        return [self.DEPARTMENT[0], self.DEPARTMENT[1].replace('{DEPARTMENT_CATEGORY}', department)]

    def verify_search_result(self, expected_result):
        self.verify_text(expected_result, *self.RESULT)

    def verify_correct_department(self, department):
        department_locator = self.get_department_locator(department)
        self.wait_for_element_appear(*department_locator)