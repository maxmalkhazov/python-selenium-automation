from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@given('open amazon help page')
def open_url(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('user inputs text in search field')
def input_keyword(context):
    search = context.driver.find_element(By.ID, "helpsearch")
    search.clear()
    search.send_keys('Cancel order', Keys.RETURN)


@then('user is redirected to matching page')
def verify_redirect_page(context):
    expected_result = 'Cancel Items or Orders'
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1[text()='Cancel Items or Orders']").text

    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
