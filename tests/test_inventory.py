import allure
import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestCartClass:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.inventory_page = InventoryPage(browser)
        self.login_page = LoginPage(browser)


    @allure.epic('US_002.00')
    @allure.story('TC_002.00.01')
    @allure.title("Bage change when adding")
    def test_change_bage_when_adding(self, browser, username='standard_user', password='secret_sauce'):
        with allure.step('step1 login user'):
            self.login_page.action_login(username, password)
        with allure.step('step2 click on add'):
            self.inventory_page.add_to_cart()
        with allure.step('step3 bage has changed'):
            self.inventory_page.bage_has_changed()


    @allure.epic('US_002.00')
    @allure.story('TC_002.00.02')
    @allure.title("Button text after remove")
    def test_change_add_button_text(self, browser, username='standard_user', password='secret_sauce'):
        with allure.step('step1 login user'):
            self.login_page.action_login(username, password)
        with allure.step('step2 text before adding'):
            self.inventory_page.button_text_before_adding()
        with allure.step('step3 click on button'):
            self.inventory_page.add_to_cart()
        with allure.step('step4 text after adding'):
            self.inventory_page.button_text_after_adding()



