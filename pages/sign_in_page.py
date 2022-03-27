from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC

class SignInPage(Page):

    def verify_sign_in_opened(self):
        self.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))