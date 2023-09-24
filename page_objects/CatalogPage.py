from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage

class CatalogPage(BasePage):
    PRODUCT_COMPARE_LINK = (By.ID, "compare-total")
    LIMIT_INPUT = (By.ID, "input-limit")
    SORT_INPUT = (By.ID, "input_sort")
    PRICE = (By.CSS_SELECTOR, "div.caption > p.price")
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@class='fa fa-shopping-cart']")
    PRODUCT_PRICE = (By.XPATH, "//*[@class='price-tax']")

    def verify_product_compare(self):
        self._element(self.PRODUCT_COMPARE_LINK)

    def verify_limit_imput(self):
        self._element(self.LIMIT_INPUT)

    def verify_sort_input(self):
        self._element(self.LIMIT_INPUT)

    def verify_price(self):
        self._element(self.PRICE)

    def verify_add_to_cart_button(self):
        self._element(self.ADD_TO_CART_BUTTON)

    def get_product_price(self):
        price = self._element(self.PRODUCT_PRICE).text
        return price
