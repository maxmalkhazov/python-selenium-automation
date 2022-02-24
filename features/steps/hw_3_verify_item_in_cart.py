from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_SUBMIT = (By.ID, 'nav-search-submit-button')
CLICK_ON_ITEM = (By.CSS_SELECTOR, '.a-section.aok-relative.s-image-square-aspect')
CLICK_ADD_TO_CART = (By.ID, 'add-to-cart-button')


@when('search for {item}')
def search_item(context, item):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(item)


@when('click search')
def click_search(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@when('click on item')
def click_on_item(context):
    context.driver.find_element(*CLICK_ON_ITEM).click()


@when('add item to cart')
def add_to_cart(context):
    button = context.driver.find_element(*CLICK_ADD_TO_CART).click()
    sleep(3)


@then('verify item exists in cart')
def verify_item_added(context):
    expected_result = '1'
    actual_result = context.driver.find_element(By.ID, 'nav-cart-count').text
    print(actual_result)
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'