from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtils:

    @staticmethod
    def wait_for_url(driver, url_part, timeout=15):
        WebDriverWait(driver, timeout).until(
            EC.url_contains(url_part)
        )

    @staticmethod
    def wait_for_element(driver, locator, timeout=15):
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @staticmethod
    def wait_for_clickable(driver, locator, timeout=15):
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )