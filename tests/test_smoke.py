import pytest
from utils.utils import ReadConfig


def test_should_be_correct_url(login_page):
    login_page.open()
    login_page.should_be_login_link()

def test_login(login_page):
    login_page.login(ReadConfig.get_standard_user_login(), ReadConfig.get_standard_user_password())

def test_should_be_inventory_list(main_page, login_page):
    login_page.login(ReadConfig.get_standard_user_login(), ReadConfig.get_standard_user_password())
    main_page.should_be_inventory_list()

# def test_add_to_cart(login_page, main_page):
