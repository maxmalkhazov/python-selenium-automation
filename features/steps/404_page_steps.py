from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


DOG_IMG = (By.CSS_SELECTOR, '#d[alt="Dogs of Amazon"]')


@given('Store original window')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@when('Click on a dog image')
def click_dog_image(context):
    context.driver.find_element(*DOG_IMG).click()


@when('Switch to new window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    print('\nCurrent:', current_windows)
    context.driver.switch_to.window(current_windows[1])


@then('Return to original window')
def switch_to_original_window(context):
    context.driver.switch_to.window(context.original_window)