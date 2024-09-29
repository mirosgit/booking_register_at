from selenium.webdriver.common.by import By


class RegisterFormLocators:

    register_button = (By.CSS_SELECTOR, "header > div > nav[class='Header_bar'] > div > a[data-testid='header-sign-up-button']")
    email_field = (By.CSS_SELECTOR, "input[name='username']")
    continue_email_button = (By.CSS_SELECTOR, "button[type='submit']")
    email_error_icon = (By.CSS_SELECTOR, "div[class='input-wrapper-email bui-spacer--large nw-login-name'] > div > div:nth-child(2) > div > div:nth-child(3) > span > svg")
    email_error_note = (By.CSS_SELECTOR, "div[id='username-note']")
    new_password_field = (By.CSS_SELECTOR, "input[name='new_password']")
    confirm_password_field = (By.CSS_SELECTOR, "input[name='confirmed_password']")
    continue_password_button = (By.CSS_SELECTOR, "button[type='submit']")
    new_password_error_icon = (By.CSS_SELECTOR, "form > div > div:nth-child(1) > div > div > div > div > div:nth-child(3) > span > svg")
    confirm_password_error_icon = (By.CSS_SELECTOR, "form > div > div:nth-child(2) > div > div > div > div > div:nth-child(3) > span > svg")
    new_password_error_note = (By.CSS_SELECTOR, "div[id='new_password-note']")

