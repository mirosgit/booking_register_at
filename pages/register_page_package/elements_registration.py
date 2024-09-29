from locators_package import RegisterFormLocators


class FindElements:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.register_locators = RegisterFormLocators()

    def find_element(self, css_selector):
        element = self.browser.find_element(*css_selector)
        return element

    def register_button(self):
        return self.find_element(self.register_locators.register_button)

    def email_field(self):
        return self.find_element(self.register_locators.email_field)

    def continue_email_button(self):
        return self.find_element(self.register_locators.continue_email_button)

    def email_error_icon(self):
        return self.find_element(self.register_locators.email_error_icon)

    def email_error_note(self):
        return self.find_element(self.register_locators.email_error_note)

    def new_password_filed(self):
        return self.find_element(self.register_locators.new_password_field)

    def confirm_password_filed(self):
        return self.find_element(self.register_locators.confirm_password_field)

    def continue_password_button(self):
        return self.find_element(self.register_locators.continue_password_button)

    def new_password_error_icon(self):
        return self.find_element(self.register_locators.new_password_error_icon)

    def confirm_password_error_icon(self):
        return self.find_element(self.register_locators.confirm_password_error_icon)

