from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class MainPage(BasePage):
    LOGO = (By.XPATH, "//*[@class='img-responsive']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//div[@class='button-group']/button[1]")
    SEARCH_BUTTON = (By.XPATH, "//*[@class='btn btn-default btn-lg']")
    CART_BUTTON = (By.XPATH, "//*[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']")
    SEARCH_INPUT = (By.ID, "search")
    PRODUCT_LAYOUT = (By.CSS_SELECTOR, "#content > div.row .product-layout .product-thumb .image > a")
    PRODUCT_PRICE = (By.XPATH, "//*[@class='price-tax']")

    def verify_logo(self):
        self._element(self.LOGO)

    def verify_add_button(self):
        self._element(self.ADD_TO_CART_BUTTON)

    def verify_search_button(self):
        self._element(self.SEARCH_BUTTON)

    def verify_search_input(self):
        self._element(self.SEARCH_INPUT)

    def verify_cart_button(self):
        self._element(self.CART_BUTTON)

    def click_add_product(self):
        self._click(self.ADD_TO_CART_BUTTON)

    def click_in_card_product(self, index: int):
        self.driver.find_elements(*self.PRODUCT_LAYOUT)[index].click()

    def get_product_price(self):
        price = self._element(self.PRODUCT_PRICE).text
        return price
