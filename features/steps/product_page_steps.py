from selenium.webdriver.common.by import By
from behave import given, when, then

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@then('Verify user can click through 3 colors')
def verify_3_colors(context):
    expected_colors = ['Black', 'Navy', 'Multicolour']
    color_options = context.driver.find_elements(*COLOR_OPTIONS)

    actual_colors = []
    for color in color_options:
        color.click()
        current_color_name = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color_name]

    assert expected_colors == actual_colors, f'Actual {actual_colors} do not match {expected_colors}'


@then('Verify user can click through 5 colors')
def verify_5_colors(context):
    expected_colors = ['Army Green', 'Black', 'Blue', 'Brown', 'Burgundy']
    color_options = context.driver.find_elements(*COLOR_OPTIONS)

    actual_colors = []
    for color in color_options[:5]:
        color.click()
        current_color_name = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color_name]

    assert expected_colors == actual_colors, f'Actual {actual_colors} do not match {expected_colors}'
