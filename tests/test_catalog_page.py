from selenium.webdriver.common.by import By


def test_catalog(browser):
    browser.get(browser.url + "/desktops")
    browser.find_element(By.ID, "compare-total")
    browser.find_element(By.XPATH, "//*[@class='col-sm-6 text-right']")
    browser.find_element(By.ID, "input-sort")
    browser.find_element(By.XPATH, "//*[@class='product-thumb']")
    browser.find_element(By.CSS_SELECTOR, "div.caption > p.price")


def test_currency_change_catalog(browser):
    browser.get(browser.url)
    browser.find_element(By.XPATH, "//*[@class='btn btn-link dropdown-toggle']").click()
    browser.find_element(By.XPATH, "//*[@class='currency-select btn btn-link btn-block']").click()
    browser.find_element(By.LINK_TEXT, 'Cameras').click()
    browser.find_element(By.XPATH, "//p[contains(.,'€')]")

