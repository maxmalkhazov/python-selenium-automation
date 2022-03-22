from selenium.webdriver.common.by import By
from behave import given, when, then


HEADER_LINKS = (By.CSS_SELECTOR, '#zg_header li')
HEADER_TITLE = (By.CSS_SELECTOR, '.a-row.a-carousel-header-row.a-size-large h2')


@given('open amazon best sellers page')
def open_best_sellers_page(context):
    context.app.bestsellers_page.open_best_sellers_page()


@then('verify there are {expected_amount} links')
def verify_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links_amount = len(context.driver.find_elements(*HEADER_LINKS))
    print(links_amount)
    assert links_amount == expected_amount, f'Expected {expected_amount} links but got {links_amount}'


@then('Click on each link and verify correct page opens')
def click_on_each_link(context):
    n = 4

    while n >= 0:
        links = []
        links += context.driver.find_elements(*HEADER_LINKS)
        links[n].click()
        assert context.driver.find_elements(By.CSS_SELECTOR, '#zg_header li')[n].text.lower() in context.driver.find_element(By.XPATH, '//h2[@class="a-carousel-heading a-inline-block"]').text.lower(), f'Page does not open'
        n = n - 1





