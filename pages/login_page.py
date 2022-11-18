from locators.login_locators import LoginLocators as ll
from core.core import Core


class LoginPage(Core):
    def __init__(self, driver):
        Core.__init__(self, driver)
        self.driver = driver

    def login_title(self):
        return self.driver.title

    def action_login(self, username, password):
        Core.send_keys(
            self, ll.input_username, username
        )
        Core(
            self, ll.input_password, password
        )
        Core.click(self, ll.login_btn)

    def action_logout(self):
        self.driver.find_element(*ll.hamburger_btn).click()
        self.driver.find_element(*ll.logout_btn).click()
