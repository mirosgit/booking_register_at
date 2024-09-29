import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from pages.user_registration import *
from parsing_data_from_file import ParseDataExcel
from locators_package import RegisterFormLocators

chrome_options = Options()
chrome_options.add_argument("--force-device-scale-factor=1")

parser = ParseDataExcel('Test_Data.xlsx')
TESTS_TO_RUN = parser.get_tests_to_run()


class TestUserRegistration:

    def setup_method(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.maximize_window()
        self.booking_page = UserRegistration(self.browser, "https://www.booking.com/")
        self.booking_page.open()

    def teardown_method(self):
        self.browser.quit()

    @allure.step("Checking the current URL against the expected URL")
    def verify_current_url(self, expected_url):
        parsed_url = urlparse(self.browser.current_url)
        url_without_params = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
        assert url_without_params == expected_url, f"Expected URL: {expected_url}, but received: {url_without_params}"

    @allure.step("Checking if the expected element is present on the page")
    def verify_element_presence(self, element_selector):
        try:
            self.browser.find_element(*element_selector)
        except NoSuchElementException:
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"Element with selector '{element_selector}' not found on the page")

    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        outcome = yield
        rep = outcome.get_result()

        if rep.when == "call" and rep.failed:
            if hasattr(self, 'browser'):
                allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.title("TEST CASE ID 2")
    @allure.description("Checking that clicking the 'Sign Up' button redirects to the registration form")
    @pytest.mark.skipif('test_case_id_2' not in TESTS_TO_RUN, reason='Not set to run in config file')
    def test_case_id_2_run(self):
        self.booking_page.pre_condition_email_page()
        self.verify_current_url("https://account.booking.com/sign-in")

    @allure.title("TEST CASE ID 3")
    @allure.description("Checking the transition to the next stage of registration after entering the correct e-mail")
    @pytest.mark.skipif('test_case_id_3' not in TESTS_TO_RUN, reason='Not set to run in config file')
    def test_case_id_3_run(self):
        self.booking_page.pre_condition_password_page()
        self.verify_current_url("https://account.booking.com/register/password")

    @allure.title("TEST CASE ID 10")
    @allure.description("Validation of system registration when required password fields are empty")
    @pytest.mark.skipif('test_case_id_10' not in TESTS_TO_RUN, reason='Not set to run in config file')
    def test_case_id_10_run(self):
        self.booking_page.pre_condition_password_page()
        self.booking_page.click_confirm_button_pass_page()
        self.verify_element_presence(RegisterFormLocators.new_password_error_note)

    @allure.title("TEST CASE ID 11")
    @allure.description("Validation of system registration when the required email field is empty")
    @pytest.mark.skipif('test_case_id_11' not in TESTS_TO_RUN, reason='Not set to run in config file')
    def test_case_id_11_run(self):
        self.booking_page.pre_condition_email_page()
        self.booking_page.click_confirm_button_email_page()
        self.verify_element_presence(RegisterFormLocators.email_error_note)
