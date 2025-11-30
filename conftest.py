import time
import pytest
from pages.login_page import LoginPage
from utils.utils import ReadConfig
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def login_page(driver):
    url = ReadConfig().get_url()
    return LoginPage(driver, url)