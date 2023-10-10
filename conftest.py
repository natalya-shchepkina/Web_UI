import logging
import datetime
import os

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver import ChromeOptions, FirefoxOptions, EdgeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"])
    parser.addoption("--url", required=True)
    parser.addoption("--test_log_level", action="store", default="INFO")
    parser.addoption("--executor", action="store", default="127.0.0.1", help="Selenoid executor")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--video", action="store_true")
    parser.addoption("--bv", action="store")
    parser.addoption("--local", action="store_true")


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--test_log_level")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")
    local = request.config.getoption("--local")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    executor_url = f"http://{executor}:4444/wd/hub"

    caps = {
            "enableVNC": vnc,
            "enableVideo": video,
            "enableLog": logs
    }

    match browser:
        case "chrome":
            options = ChromeOptions()
            if local:
                driver = webdriver.Chrome(options=options)
            else:
                options.set_capability("browserName", browser)
                options.browser_version = version
                options.set_capability("selenoid:options", caps)
                driver = webdriver.Remote(
                    command_executor=executor_url,
                    options=options
                )
        case "firefox":
            options = FirefoxOptions()
            if local:
                driver = webdriver.Firefox(options=options)
            else:
                options.set_capability("browserName", browser)
                options.browser_version = version
                options.set_capability("selenoid:options", caps)
                driver = webdriver.Remote(
                    command_executor=executor_url,
                    options=options
                )
        case _:
            raise ValueError(f'Browser {browser} not support')

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name
    driver.get(url)
    driver.url = url

    driver.maximize_window()
    logger.info("Browser %s started" % browser)

    request.addfinalizer(driver.close)
    return driver
