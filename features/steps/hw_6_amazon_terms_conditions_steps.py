from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


PRIVATE_LINK = (By.XPATH, '//div[@class="help-service-content"]// a[text()="Privacy Notice"]')
PRIVACY_HEADER = (By.CSS_SELECTOR, '.help-content h1')


@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_original_windows(context):
    context.original_window = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def click_on_privacy_link(context):
    context.driver.find_element(*PRIVATE_LINK).click()


@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    context.driver.switch_to.window(current_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_amazon_privacy_page_opened(context):
    context.driver.wait.until(
        EC.text_to_be_present_in_element((PRIVACY_HEADER), 'Amazon.com Privacy Notice'),
        message="Page not found")


@then('User can close new window and switch back to original')
def close_new_window_switch_to_original(context):
    context.driver.switch_to.window(context.original_window)