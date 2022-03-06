from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

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


@then('Verify that SignIn popup shown')
def verify_sign_in_shown(context):
    context.driver.wait.until(EC.visibility_of_element_located(SIGN_IN_POPUP_BTN), message="SignIn not shown")


@then('Verify that SignIn btn is clickable')
def verify_sign_in_btn_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN), message="SignIn btn not clickable")


@when('Wait for {sec} seconds')
def wait(context, sec):
    sleep(int(sec))


@then('Verify that Signin popup disappears')
def verify_that_signin_popup_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN_POPUP_BTN), message="SignIn popup does not disappear")