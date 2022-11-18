# from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import logging


class Core:
    LOGGER = logging.getLogger(__name__)

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, wait=5):
        try:
            self.LOGGER.info("local core.find_element method")
            return WebDriverWait(self.driver, timeout=wait).until(
                lambda d: d.find_element(*locator)
            )
        except NoSuchElementException as e:
            self.LOGGER.error(f"NoSuchElementException: {e}")

    def send_keys(self, locator, value, wait=5):
        try:
            self.find_element(locator, wait).send_keys(value)
        except Exception as e:
            self.LOGGER.error(f"Exception: {e}")

    def click(self, locator, wait=5):
        try:
            self.find_element(locator, wait).click()
        except Exception as e:
            self.LOGGER.error(f"Exception: {e}")
