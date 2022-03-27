from selenium.webdriver.common.by import By
from behave import given, when, then




CLICK_CART = (By.ID, 'nav-cart')
CART_COUNT = (By.ID, 'nav-cart-count')


@when('click on cart icon')
def click_cart(context):
    context.app.header.wait_for_element_click(*CLICK_CART)


@then('verify cart is empty')
def verify_empty_cart(context):

    context.app.header.verify_empty_cart()