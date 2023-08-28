from selenium.webdriver.common.by import By


def test_admin_page(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(By.ID, "input-username")
    browser.find_element(By.ID, "input-password")
    browser.find_element(By.LINK_TEXT, "Forgotten Password")
    browser.find_element(By.XPATH, "//*[@class='btn btn-primary']")
    browser.find_element(By.CSS_SELECTOR, "#footer > a")


def test_user_login(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(By.ID, "input-username").send_keys("user")
    browser.find_element(By.ID, "input-password").send_keys("bitnami")
    browser.find_element(By.XPATH, "//*[@class='btn btn-primary']").click()
    browser.find_element(By.XPATH, "//*[@class='fa fa-sign-out']").click()


