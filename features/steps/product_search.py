from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')

@given('open amazon homepage')
def open_amazon_homepage(context):
    context.app.main_page.open_main()

@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_BUTTON).click()


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), f"{search_word} not in {context.driver.current_url.lower()}"
