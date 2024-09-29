import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from pages.user_registration import *
from parsing_data_from_file import ParseDataExcel

chrome_options = Options()
chrome_options.add_argument("--force-device-scale-factor=1")

parser = ParseDataExcel('Test_Data.xlsx')
TESTS_TO_RUN = parser.get_tests_to_run()


class TestUserRegistration:

    def setup_method(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.link_booking_page = "https://www.booking.com/"
        self.booking_page = UserRegistration(self.browser, self.link_booking_page)
        self.booking_page.open()
        self.open_browser_full_screen()

    def open_browser_full_screen(self):
        self.browser.maximize_window()

    def teardown_method(self):
        self.browser.quit()

    @allure.step("Checking the current URL against the expected URL")
    def verify_current_url(self, expected_url):
        parsed_url = urlparse(self.browser.current_url)
        url_without_params = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
        assert url_without_params == expected_url, f"Expected URL: {expected_url}, but received: {url_without_params}"

    @allure.title("TEST CASE ID 2")
    @allure.description("Checking that clicking the 'Sign Up' button redirects to the registration form")
    @pytest.mark.skipif('test_case_id_2' not in TESTS_TO_RUN, reason='Not set to run in config file')
    def test_case_id_2_run(self):
        self.booking_page.pre_condition_id_2()
        try:
            self.verify_current_url("https://account.booking.com/sign-in")
        except AssertionError as e:
            allure.attach(self.browser.get_screenshot_as_png(), name="Screen", attachment_type=allure.attachment_type.PNG)
            raise e

    @allure.title("TEST CASE ID 3")
    @allure.description("Checking the transition to the next stage of registration after entering the correct e-mail")
    @pytest.mark.skipif('test_case_id_3' not in TESTS_TO_RUN, reason='Not set to run in config file')
    def test_case_id_3_run(self):
        self.booking_page.pre_condition_id_3()
        try:
            self.verify_current_url("https://account.booking.com/register/password")
        except AssertionError as e:
            allure.attach(self.browser.get_screenshot_as_png(), name="Screen", attachment_type=allure.attachment_type.PNG)
            raise e
