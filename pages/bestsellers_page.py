from pages.base_page import Page
from selenium.webdriver.common.by import By


class BestsellersPage(Page):
    HEADER_LINKS = (By.CSS_SELECTOR, '#zg_header li')
    HEADER_TITLE = (By.CSS_SELECTOR, '.a-row.a-carousel-header-row.a-size-large h2')

    def open_best_sellers_page(self):
        self.open_url(end_url='gp/bestsellers/?ref_=nav_cs_bestsellers')

    def verify_links(self, expected_amount):
        expected_amount = int(expected_amount)
        links_amount = len(self.driver.find_elements(*self.HEADER_LINKS))
        print(links_amount)
        assert links_amount == expected_amount, f'Expected {expected_amount} links but got {links_amount}'

    def click_on_each_link(self):
        n = 4

        while n >= 0:
            links = []
            links += self.driver.find_elements(*self.HEADER_LINKS)
            links[n].click()
            assert self.driver.find_elements(By.CSS_SELECTOR, '#zg_header li')[n].text.lower() in self.driver.find_element(By.XPATH,'//h2[@class="a-carousel-heading a-inline-block"]').text.lower(), f'Page does not open'
            n = n - 1


