import time
import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.purchase_complete_page import PurchaseCompletePage
from pages.purchase_page import PurchasePage
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
    url = ReadConfig().get_url()
    return MainPage(driver, url)

@pytest.fixture(scope='function')
def cart_page(driver):
    url = ReadConfig().get_url()
    return CartPage(driver, url)

@pytest.fixture(scope='function')
def checkout_page(driver):
    url = ReadConfig().get_url()
    return CheckoutPage(driver, url)

@pytest.fixture(scope='function')
def purchase_page(driver):
    url = ReadConfig().get_url()
    return PurchasePage(driver, url)

@pytest.fixture(scope='function')
def purchase_complete_page(driver):
    url = ReadConfig().get_url()
    return PurchaseCompletePage(driver, url)