from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_TEXT = (By.CSS_SELECTOR, '.a-size-small.a-color-tertiary.wfm-sales-item-card__regular-price')
PRODUCT_NAME = (By.CSS_SELECTOR, '.wfm-sales-item-card__product-name')


@given('Open Whole Foods Promo page')
def open_whole_foods_promo_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')
    context.driver.find_element(By.XPATH, '//span[@class="a-button a-spacing-top-base a-button-base glow-toaster-button glow-toaster-button-dismiss"]').click()


@then('Verify product has a text "Regular"')
def verify_product_text(context):
    product_text = context.driver.find_elements(*PRODUCT_TEXT)
    expected_result = 'Regular'

    for t in product_text:
        print(t.text)
        assert expected_result.lower() in t.text.lower(), f'{expected_result} not found in product'


@then('Verify product has a product name')
def verify_product_name(context):
    product_name = context.driver.find_elements(*PRODUCT_NAME)

    for item in product_name:
        print(item.text)
        assert len(item.text) > 0, f'No product name'


