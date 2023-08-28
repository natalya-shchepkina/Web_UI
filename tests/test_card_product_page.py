from selenium.webdriver.common.by import By


def test_card_product(browser):
    browser.get(browser.url + "/desktops/htc-touch-hd")
    browser.find_element(By.ID, "button-cart")
    browser.find_element(By.ID, "input-quantity")
    browser.find_element(By.ID, "product")
    browser.find_element(By.XPATH, "//*[@class='rating']")
    browser.find_element(By.XPATH, "//*[@class='btn-group']")
