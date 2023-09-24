from selenium.webdriver.common.by import By

from page_objects.AdminPage import AdminPage


class AdminMenu(AdminPage):
    CATALOG = (By.ID, "menu-catalog")
    PRODUCTS = (By.XPATH, "//a[contains(.,'Products')]")

    def go_to_catalog(self):
        self._click(self.CATALOG)

    def go_to_products_catalog(self):
        self.go_to_catalog()
        self._click(self.PRODUCTS)





