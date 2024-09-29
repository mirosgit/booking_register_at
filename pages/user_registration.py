import time
from .register_page_package import FindElements, UserRegistrationWait
from .base_page import BasePage
from faker import Faker

fake = Faker()


class UserRegistration(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.find_elements_register_form = FindElements(browser=self.browser, url=self.url)
        self.wait_until_register_form = UserRegistrationWait(browser=self.browser, url=self.url)

    def go_to_email_page(self):
        """ Test case to interact with the registration form """
        self.wait_until_register_form.wait_register_button()
        self.find_elements_register_form.register_button().click()

        # time.sleep(10)
