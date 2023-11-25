import allure

from page_objects.elemets.AlertElement import SuccessAlert

from page_objects.MainPage import MainPage
from page_objects.elemets.TopMenu import TopMenu


@allure.step("Test the visibility of element on main page")
def test_main_page(browser):
    main_page = MainPage(browser)
    main_page.verify_add_button()
    main_page.verify_cart_button()
    main_page.verify_logo()
    main_page.verify_search_button()
    main_page.verify_search_input()


@allure.step("Test the adding product")
def test_add_product(browser):
    MainPage(browser).click_add_product()
    assert SuccessAlert(browser).verify_success_alert()


@allure.step("Test the change currency")
def test_currency_change(browser):
    TopMenu(browser).choice_currency()
    selected_currency = TopMenu(browser).get_currency_name()
    product_price = MainPage(browser).get_product_price()
    assert selected_currency[0] in product_price

