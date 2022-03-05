from selenium.webdriver.common.by import By
from behave import given, when, then

HEADER_LINKS = (By.CSS_SELECTOR, '#zg_header li')

@given('open amazon best sellers page')
def open_best_sellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('verify there are {expected_amount} links')
def verify_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links_amount = len(context.driver.find_elements(*HEADER_LINKS))
    print(links_amount)
    assert links_amount == expected_amount, f'Expected {expected_amount} links but got {links_amount}'