import allure
from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class AdminPage(BasePage):
    ADD_BUTTON = (By.XPATH, "//*[@class='pull-right']/a")
    SAVE_BUTTON = (By.XPATH, "//*[@class='pull-right']/button")
    DELETE_BUTTON = (By.XPATH, "//*[@data-original-title='Delete']")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")

    # product form
    TAB_DATA = (By.XPATH, "//a[contains(.,'Data')]")
    PRODUCT_NAME_INPUT = (By.ID, "input-name1")
    PRODUCT_MODEL_INPUT = (By.ID, "input-model")
    PRODUCT_META_TITLE = (By.ID, "input-meta-title1")

    # product list
    TABLE_CHECKBOX = (By.XPATH, "//td[contains(.,'name')]/../td")

    @allure.step("Add new product")
    def add_new_product(self):
        self.logger.debug("%s: Add new product" % self.class_name)
        self._click(self.ADD_BUTTON)
        self._input(self.PRODUCT_NAME_INPUT, "name")
        self._input(self.PRODUCT_META_TITLE, "name")
        self._click(self.TAB_DATA)
        self._input(self.PRODUCT_MODEL_INPUT, "model")
        self._click(self.SAVE_BUTTON)

    def verify_success_alert(self):
        return self._element(self.SUCCESS_ALERT)

    @allure.step("Delete product")
    def delete_product(self):
        self.logger.debug("%s: Delete product" % self.class_name)
        self._click(self.TABLE_CHECKBOX)
        self._click(self.DELETE_BUTTON)
        self.driver.switch_to.alert.accept()








