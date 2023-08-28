from selenium.webdriver.common.by import By


def test_register_page(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    browser.find_element(By.ID, "account")
    browser.find_element(By.ID, "input-password")
    browser.find_element(By.XPATH, "//*[@class='radio-inline']")
    browser.find_element(By.XPATH, "//*[@class='btn btn-primary']")
    browser.find_element(By.XPATH, "//*[@class='agree']")
