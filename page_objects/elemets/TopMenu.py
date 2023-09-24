import random

from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class TopMenu(BasePage):
    # top menu
    CURRENCY_DROPDOWN = (By.XPATH, "//*[@class='btn btn-link dropdown-toggle']")
    CURRENCY_EUR = (By.XPATH, "//button[@name='EUR']")
    CURRENCY_GBP = (By.XPATH, "//*//button[@name='GBP']")
    CURRENCY_USD = (By.XPATH, "//*//button[@name='USD']")
    CURRENCY_LIST = [
        CURRENCY_EUR,
        CURRENCY_GBP,
        CURRENCY_USD
    ]


    # main menu
    TABLETS_LINK = (By.LINK_TEXT, 'Tablets')
    PHONES_LINK = (By.LINK_TEXT, 'Phones & PDAs')
    CAMERAS_LINK = (By.LINK_TEXT, 'Cameras')
    MAIN_MENU_LINKS = [
        TABLETS_LINK,
        PHONES_LINK,
        CAMERAS_LINK
    ]

    def choice_currency(self):
        self._click(self.CURRENCY_DROPDOWN)
        self._click(self.CURRENCY_LIST[random.randint(0, 2)])

    def get_currency_name(self):
        name = self._element(self.CURRENCY_DROPDOWN).text
        return name

    def go_to_directory(self):
        self._click(self.MAIN_MENU_LINKS[random.randint(0, 2)])
