from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-button')

@given('open amazon homepage')
def open_amazon_homepage(context):
    context.driver.get('https://www.amazon.com/')


@when('click on button from signin popup')
def click_signin_popup(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_POPUP_BTN),
        message='Sign in button not clickable'
    ).click()


@then('verify sign in page is opened')
def verify_sign_in_opened(context):
    context.driver.wait.until(
        EC.url_contains('https://www.amazon.com/ap/signin'),
        message="Sign in page does not open")