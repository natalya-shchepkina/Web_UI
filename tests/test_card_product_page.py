import random

import allure

from page_objects.CardProductPage import CardProductPage
from page_objects.MainPage import MainPage


@allure.step("Test the visibility of element on product page")
def test_card_product(browser):
    MainPage(browser).click_in_card_product(random.randint(0, 3))
    CardProductPage(browser).verify_add_to_cart_button()
    CardProductPage(browser).verify_compare_product_button()
    CardProductPage(browser).verify_wishlist_button()
    CardProductPage(browser).verify_quantity_input()
    CardProductPage(browser).verify_thumbnail()