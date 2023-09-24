from page_objects.RegisterPage import RegisterPage


def test_register_page(browser):
    RegisterPage(browser).open(browser.url)
    RegisterPage(browser).verify_main_element()


def test_register_user(browser):
    RegisterPage(browser).open(browser.url)
    RegisterPage(browser).register_user()
    RegisterPage(browser).get_success_text()

