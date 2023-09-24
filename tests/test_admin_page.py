from page_objects.AdminPage import AdminPage
from page_objects.LoginPage import LoginPage
from page_objects.elemets.AdminMenu import AdminMenu


def test_create_new_product(browser):
    LoginPage(browser).authorization(browser.url)
    AdminMenu(browser).go_to_products_catalog()
    AdminPage(browser).add_new_product()

    assert AdminPage(browser).verify_success_alert()


def test_delete_product(browser):
    LoginPage(browser).authorization(browser.url)
    AdminMenu(browser).go_to_products_catalog()
    AdminPage(browser).add_new_product()
    AdminPage(browser).delete_product()
    AdminPage(browser).verify_success_alert()

    assert AdminPage(browser).verify_success_alert()
