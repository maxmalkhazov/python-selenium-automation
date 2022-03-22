
from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")

    def verify_search_result(self, expected_result):
        self.verify_text(expected_result, *self.RESULT)