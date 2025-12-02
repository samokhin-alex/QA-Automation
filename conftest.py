import time
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
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

@pytest.fixture(scope='function')
def main_page(driver):
    url = ReadConfig().get_inventory_url()
    return MainPage(driver, url)