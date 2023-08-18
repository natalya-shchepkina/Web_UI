
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.safari.service import Service as SafariService


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", choices=["chrome", "firefox"]
    )

    parser.addoption(
        "--url", default="http://192.168.0.101:8081"
    )


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser_name == "chrome":
        service = ChromiumService()
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FFService()
        driver = webdriver.Firefox(service=service)
    else:
        raise NotImplemented()

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver