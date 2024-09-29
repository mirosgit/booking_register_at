import time
from .register_page_package import FindElements, UserRegistrationWait
from .register_page_package import FakeDynamicData
from .base_page import BasePage
from faker import Faker

fake = Faker()


class UserRegistration(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.find_elements_register_form = FindElements(browser=self.browser, url=self.url)
        self.wait_until_register_form = UserRegistrationWait(browser=self.browser, url=self.url)
        self.fake_dynamic_data = FakeDynamicData()

    def pre_condition_email_page(self):
        self.wait_until_register_form.wait_register_button()
        self.find_elements_register_form.register_button().click()
        self.wait_until_register_form.wait_email_field()

    def pre_condition_password_page(self):
        self.wait_until_register_form.wait_register_button()
        self.find_elements_register_form.register_button().click()
        self.wait_until_register_form.wait_email_field()
        self.find_elements_register_form.email_field().send_keys(self.fake_dynamic_data.generate_random_email())
        self.find_elements_register_form.continue_email_button().click()
        self.wait_until_register_form.wait_password_field()

    def click_confirm_button_pass_page(self):
        self.find_elements_register_form.continue_password_button().click()

    def click_confirm_button_email_page(self):
        self.find_elements_register_form.continue_email_button().click()


