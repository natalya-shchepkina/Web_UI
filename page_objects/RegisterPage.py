import allure
from selenium.webdriver.common.by import By

from data.user_data import User
from page_objects.BasePage import BasePage


class RegisterPage(BasePage):
    PATH = "/index.php?route=account/register"

    FIRSTNAME_INPUT = (By.ID, "input-firstname")
    LASTNAME_INPUT = (By.ID, "input-lastname")
    PASSWORD_INPUT = (By.ID, "input-password")
    EMAIL_INPUT = (By.ID, "input-email")
    TELEPHONE_INPUT = (By.ID, "input-telephone")
    CONFIRM_INPUT = (By.ID, "input-confirm")
    PRIVACY_POLICY_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
    CONTINUE_BUTTON = (By.XPATH, "//*[@class='btn btn-primary']")
    SUCCESS_TEXT = (By.XPATH, "//*[contains(.,'Your Account Has Been Created!')]")

    def open(self, url):
        self.driver.get(url + self.PATH)

    def verify_main_element(self):
        self._element(self.FIRSTNAME_INPUT)
        self._element(self.LASTNAME_INPUT)
        self._element(self.EMAIL_INPUT)
        self._element(self.PASSWORD_INPUT)
        self._element(self.TELEPHONE_INPUT)
        self._element(self.CONFIRM_INPUT)
        self._element(self.PRIVACY_POLICY_CHECKBOX)
        self._element(self.CONTINUE_BUTTON)

    @allure.step("Register user")
    def register_user(self):
        self.logger.debug("%s: User registration: %s %s" % (self.class_name, User.first_name, User.last_name))
        self._input(self.FIRSTNAME_INPUT, User.first_name)
        self._input(self.LASTNAME_INPUT, User.last_name)
        self._input(self.EMAIL_INPUT, User.email)
        self._input(self.TELEPHONE_INPUT, User.telephone)
        self._input(self.PASSWORD_INPUT, User.password)
        self._input(self.CONFIRM_INPUT, User.password)
        self._click(self.PRIVACY_POLICY_CHECKBOX)
        self._click(self.CONTINUE_BUTTON)

    def get_success_text(self):
        self._element(self.SUCCESS_TEXT)
