from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon page')
def open_google(context):
    context.driver.get('https://www.amazon.com/')


@when('Click Orders')
def click_orders(context):
    search = context.driver.find_element(By.ID, "nav-orders")
    search.click()


@then('Verify Sign in page opened')
def verify_sign_in(context):
    expected_result = 'Sign-in'
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    print(actual_result)
    assert expected_result.lower() == actual_result.lower()