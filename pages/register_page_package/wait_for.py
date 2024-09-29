from locators_package import RegisterFormLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class UserRegistrationWait:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.register_page_element = RegisterFormLocators()

    def wait_register_button(self, timeout=30):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(EC.element_to_be_clickable(self.register_page_element.register_button),
                              "Could not find Register Button")

    def wait_email_field(self, timeout=30):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(EC.element_to_be_clickable(self.register_page_element.email_field),
                              "Could not find Email Field")

    def wait_password_field(self, timeout=30):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(EC.element_to_be_clickable(self.register_page_element.new_password_field),
                              "Could not find Password Field")
