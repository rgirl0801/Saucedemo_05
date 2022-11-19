from selenium.webdriver.common.by import By

from locators.locators import InventoryLocators as il


class InventoryPage():
    def __init__(self, browser):
        self.browser = browser

    def add_to_cart(self):
        self.browser.find_element(*il.ADD_BUTTON).click()


    def button_text_before_adding(self):
        assert 'ADD TO CART' in self.browser.find_element(*il.ADD_BUTTON).text, "Incorrect text"

    def button_text_after_adding(self):
        assert 'REMOVE' in self.browser.find_element(*il.REMOVE_BUTTON).text, \
            "Incorrect text"

    def bage_has_changed(self):
        assert '1' in self.browser.find_element(*il.CART_BAGE).text, \
            "Incorrect count"

    def sort_by_AZ(self):
        self.browser.find_element(*il.AZ_BUTTON).click()

    def sort_by_ZA(self):
        self.browser.find_element(*il.ZA_BUTTON).click()

    def sort_by_ASC(self):
        self.browser.find_element(*il.ASC_BUTTON).click()

    def sort_by_DESC(self):
        self.browser.find_element(*il.DESC_BUTTON).click()

    def show_sorted_elements(self):
        sorted_list = []
        for option in self.browser.find_elements(*il.ALL_PRODUCTS):
            sorted_list.append(option.text)
        return sorted_list
