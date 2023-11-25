import allure

from page_objects.elemets.AdminHeader import AdminHeader
from page_objects.LoginPage import LoginPage


@allure.step("Test the visibility of element on admin page")
def test_admin_page(browser):
    admin_page = LoginPage(browser)
    admin_page.open(browser.url)
    admin_page.verify_input_username()
    admin_page.verify_input_password()
    admin_page.verify_submit_login()
    admin_page.verify_forgotten_password()


@allure.step("Test the login of user")
def test_user_login(browser):
    login_page = LoginPage(browser)
    login_page.authorization(browser.url)
    AdminHeader(browser).logout_user()
