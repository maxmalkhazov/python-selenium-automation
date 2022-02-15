from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CLICK_CART = (By.ID, 'nav-cart')


@given('open amazon home page')
def open_url(context):
    context.driver.get('https://www.amazon.com/')


@when('click on cart icon')
def click_cart(context):
    context.driver.find_element(*CLICK_CART).click()
    sleep(1)


@then('verify cart is empty')
def verify_empty_cart(context):
    expected_result = '0'
    actual_result = context.driver.find_element(By.ID, 'nav-cart-count').text
    print(actual_result)
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
    print('Test case passed')