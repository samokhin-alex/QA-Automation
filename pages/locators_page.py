from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER_NAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

class MainPageLocators:
    LOGO_TEXT = (By.CSS_SELECTOR, '[class="header_label"] [class="app_logo"]')
    INVENTORY_LIST = (By.CSS_SELECTOR, '[class="inventory_list"]')