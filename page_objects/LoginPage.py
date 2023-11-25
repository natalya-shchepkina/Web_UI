import allure
from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class LoginPage(BasePage):
    PATH = "/admin"
    USER = "user"
    PASSWORD = "bitnami"
    INPUT_USERNAME = (By.ID, "input-username")
    INPUT_PASSWORD = (By.ID, "input-password")
    SUBMIT_LOGIN = (By.XPATH, "//*[@class='btn btn-primary']")
    FORGOTTEN_PASSWORD = (By.XPATH, "//a[contains(.,'Forgotten Password')]")

    def open(self, url):
        self.driver.get(url + self.PATH)

    @allure.step("Authorization")
    def authorization(self, url):
        self.logger.debug("%s: User authorization: %s" % (self.class_name, self.USER))
        self.open(url)
        self._input(self.INPUT_USERNAME, self.USER)
        self._input(self.INPUT_PASSWORD, self.PASSWORD)
        self._element(self.SUBMIT_LOGIN).click()

    def verify_forgotten_password(self):
        self._element(self.FORGOTTEN_PASSWORD).click()

    def verify_input_username(self):
        self._element(self.INPUT_USERNAME)

    def verify_input_password(self):
        self._element(self.INPUT_PASSWORD)

    def verify_submit_login(self):
        self._element(self.SUBMIT_LOGIN)
