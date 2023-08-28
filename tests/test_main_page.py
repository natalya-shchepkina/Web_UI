from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser):
    browser.get(browser.url)
    browser.find_element(By.XPATH, "//*[@class='btn btn-default btn-lg']")
    browser.find_element(By.XPATH, "//*[@class='img-responsive']")
    browser.find_element(By.XPATH, "//*[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']")
    browser.find_element(By.ID, "search")
    browser.find_element(By.LINK_TEXT, "OpenCart")


def test_add_product(browser):
    browser.get(browser.url)
    browser.find_element(By.XPATH, "//div[@class='button-group']/button").click()
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(.,' 1 item')]")))


def test_currency_change(browser):
    browser.get(browser.url)
    browser.find_element(By.XPATH, "//*[@class='btn btn-link dropdown-toggle']").click()
    browser.find_element(By.XPATH, "//*[@class='currency-select btn btn-link btn-block']").click()
    browser.find_element(By.XPATH, "//p[contains(.,'€')]")


