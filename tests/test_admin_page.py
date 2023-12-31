import allure

from page_objects.AdminPage import AdminPage
from page_objects.LoginPage import LoginPage
from page_objects.elemets.AdminMenu import AdminMenu


@allure.step("Test the addition of a new product")
def test_create_new_product(browser):
    LoginPage(browser).authorization(browser.url)
    AdminMenu(browser).go_to_products_catalog()
    AdminPage(browser).add_new_product()

    assert AdminPage(browser).verify_success_alert()

@allure.step("Test the deleting of a new product")
def test_delete_product(browser):
    LoginPage(browser).authorization(browser.url)
    AdminMenu(browser).go_to_products_catalog()
    AdminPage(browser).add_new_product()
    AdminPage(browser).delete_product()
    AdminPage(browser).verify_success_alert()

    assert AdminPage(browser).verify_success_alert()
