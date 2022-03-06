from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

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


@when('click on item')
def click_on_item(context):
    context.driver.find_element(*CLICK_ON_ITEM).click()


@when('add item to cart')
def add_to_cart(context):
    button = context.driver.find_element(*CLICK_ADD_TO_CART).click()


@then('verify item exists in cart')
def verify_item_added(context):
    assert context.driver.wait.until(
        EC.text_to_be_present_in_element((By.ID, 'nav-cart-count'), '1'),
        message="Item was not added to cart")