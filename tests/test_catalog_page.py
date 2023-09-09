from page_objects.CatalogPage import CatalogPage
from page_objects.elemets.TopMenu import TopMenu


def test_catalog(browser):
    TopMenu(browser).go_to_directory()
    CatalogPage(browser).verify_add_to_cart_button()
    CatalogPage(browser).verify_limit_imput()
    CatalogPage(browser).verify_price()
    CatalogPage(browser).verify_product_compare()
    CatalogPage(browser).verify_sort_input()


def test_currency_change_catalog(browser):
    TopMenu(browser).choice_currency()
    selected_currency = TopMenu(browser).get_currency_name()
    TopMenu(browser).go_to_directory()
    product_price = CatalogPage(browser).get_product_price()
    assert selected_currency[0] in product_price


