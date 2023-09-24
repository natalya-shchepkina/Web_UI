import random

from page_objects.CardProductPage import CardProductPage
from page_objects.MainPage import MainPage


def test_card_product(browser):
    MainPage(browser).click_in_card_product(random.randint(0, 3))
    CardProductPage(browser).verify_add_to_cart_button()
    CardProductPage(browser).verify_compare_product_button()
    CardProductPage(browser).verify_wishlist_button()
    CardProductPage(browser).verify_quantity_input()
    CardProductPage(browser).verify_thumbnail()