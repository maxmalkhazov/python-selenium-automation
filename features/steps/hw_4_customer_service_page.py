from selenium.webdriver.common.by import By
from behave import given, when, then

PRIMARY_HEADER = (By.XPATH, '//div[@class="a-section a-spacing-extra-large a-spacing-top-extra-large ss-landing-container"]/h1')
CONTENT_TABLE_ITEMS = (By.CSS_SELECTOR, '.a-box.self-service-rich-card')
SEARCH_FIELD = (By.ID, 'helpsearch')
SECONDARY_HEADER = (By.XPATH, '//div[@class="a-span12 a-column a-spacing-top-small"]/h1')
MENU_ITEMS = (By.CSS_SELECTOR, '#category-section li')


@given('open amazon customer service page')
def open_customer_service_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@then('verify primary header is present')
def verify_primary_header(context):
    expected_result = "Hello. What can we help you with?"
    actual_result = context.driver.find_element(*PRIMARY_HEADER).text
    assert expected_result.lower() == actual_result.lower(), f'Expected {expected_result} but got {actual_result}'


@then('verify {amount} help content boxes are present')
def verify_help_content_table(context, amount):
    expected_amount = int(amount)
    boxes_amount = len(context.driver.find_elements(*CONTENT_TABLE_ITEMS))
    assert expected_amount == boxes_amount, f'Expected {expected_amount} boxes but got {boxes_amount} boxes'


@then('verify search help field is present')
def verify_search_field(context):
    actual_result = context.driver.find_element(*SEARCH_FIELD)
    assert actual_result, f'{actual_result} not found'


@then('verify secondary header is present')
def verify_secondary_header(context):
    expected_result = "Browse Help Topics"
    actual_result = context.driver.find_element(*SECONDARY_HEADER).text
    assert expected_result.lower() == actual_result.lower(), f'Expected {expected_result} but got {actual_result}'


@then('verify {amount} support help topics menu is present')
def verify_support_menu(context, amount):
    expected_amount = int(amount)
    menu_items = len(context.driver.find_elements(*MENU_ITEMS))
    assert expected_amount == menu_items, f'Expected {expected_amount} but got {menu_items}'