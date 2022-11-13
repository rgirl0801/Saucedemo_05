from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import logging


class Core:
    LOGGER = logging.getLogger(__name__)

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        try:
            self.LOGGER.info(f"local core.find_element method")
            return WebDriverWait(self.driver, timeout=5).until(
                lambda d: d.find_element(locator[0], locator[1])
            )
        except NoSuchElementException as e:
            self.LOGGER.error(f"NoSuchElementException: {e}")

    def send_keys(self, locator, value):
        try:
            self.find_element(locator).send_keys(value)
        except Exception as e:
            self.LOGGER.error(f"Exception: {e}")

    def click(self, locator):
        try:
            self.find_element(locator).click()
        except Exception as e:
            self.LOGGER.error(f"Exception: {e}")
