from selenium.webdriver.common.by import By
from behave import given, when, then

@given('open amazon home page')
def open_url(context):
    context.driver.get('https://www.amazon.com/')


@when('click on cart icon')
def click_cart(context):
    cart = context.driver.find_element(By.ID, 'nav-cart')
    cart.click()


@then('verify cart is empty')
def verify_cart(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.XPATH, '//div[@class="a-row sc-your-amazon-cart-is-empty"]/h2').text
    print(actual_result)

    assert actual_result.lower() == expected_result.lower(), f' Expected {expected_result}, but got {actual_result}'