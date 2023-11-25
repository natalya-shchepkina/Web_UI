import allure

from page_objects.RegisterPage import RegisterPage


@allure.step("Test the visibility of element on register page")
def test_register_page(browser):
    RegisterPage(browser).open(browser.url)
    RegisterPage(browser).verify_main_element()


@allure.step("Test the register user")
def test_register_user(browser):
    RegisterPage(browser).open(browser.url)
    RegisterPage(browser).register_user()
    RegisterPage(browser).get_success_text()


