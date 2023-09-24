from selenium.webdriver.common.by import By

from page_objects.AdminPage import AdminPage


class AdminHeader(AdminPage):
    LOGOUT_USER = (By.XPATH, "//*[@class='fa fa-sign-out']")

    def logout_user(self):
        self._click(self.LOGOUT_USER)
