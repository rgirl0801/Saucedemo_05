import time

from locators.locators import LoginLocators as ll


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login_title(self):
        return self.browser.title

    def action_login(self, username, password):
        self.browser.find_element(*ll.input_username).send_keys(username)
        self.browser.find_element(*ll.input_password).send_keys(password)
        self.browser.find_element(*ll.login_btn).click()

    def action_logout(self):
        self.browser.find_element(*ll.hamburger_btn).click()
        self.browser.find_element(*ll.logout_btn).click()
