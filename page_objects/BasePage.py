from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def _verify_element_presence(self, locator):
        try:
            return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        except Exception:
            raise AssertionError("Can not find element")

    def _element(self, locator):
        return self._verify_element_presence(locator)

    def _click(self, locator):
        return self._verify_element_presence(locator).click()

    def _input(self, locator, text):
        element = self._element(locator)
        element.click()
        element.clear()
        element.send_keys(text)

