from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class CardProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")
    QUANTITY_INPUT = (By.ID, "input-quantity")
    THUMBNAIL = (By.XPATH, "//a[@class='thumbnail']")
    GROUP_BUTTON = (By.XPATH, "//*[@class='btn btn-default']")

    def verify_add_to_cart_button(self):
        self._element(self.ADD_TO_CART_BUTTON)

    def verify_quantity_input(self):
        self._element(self.QUANTITY_INPUT)

    def verify_thumbnail(self):
        self._element(self.THUMBNAIL)

    def verify_wishlist_button(self):
        button = self.driver.find_elements(*self.GROUP_BUTTON)[0]

    def verify_compare_product_button(self):
        button = self.driver.find_elements(*self.GROUP_BUTTON)[1]