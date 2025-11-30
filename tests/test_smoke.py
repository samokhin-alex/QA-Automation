from pages.login_page import LoginPage
from selenium import webdriver
import pytest
from utils.utils import ReadConfig

def test_should_be_correct_url(login_page):
    login_page.open()
    login_page.should_be_login_link()