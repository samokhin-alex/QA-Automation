from pywin.dialogs.ideoptions import buttonControlMap
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators_page import CheckoutPageLocators
from utils.utils import ReadConfig


class CheckoutPage(BasePage):
    def fill_valid_checkout_information(self):
        # self.handle_alert()
        self.type_text(CheckoutPageLocators.FIRST_NAME_INPUT_FIELD, ReadConfig.get_valid_first_name())
        self.type_text(CheckoutPageLocators.LAST_NAME_INPUT_FIELD, ReadConfig.get_valid_last_name())
        self.type_text(CheckoutPageLocators.POSTAL_CODE_INPUT_FIELD, ReadConfig.get_valid_postal_code())

    def should_be_filled_all_checkout_information(self):
        first_name = self.driver.find_element(*CheckoutPageLocators.FIRST_NAME_INPUT_FIELD).get_attribute('value')
        assert first_name == ReadConfig.get_valid_first_name(), f'First_Name не совпадают. Введено {first_name}'
        last_name = self.driver.find_element(*CheckoutPageLocators.LAST_NAME_INPUT_FIELD).get_attribute('value')
        assert last_name == ReadConfig.get_valid_last_name(), f'Last_Name не совпадают. Введено {last_name}'
        postal_code = self.driver.find_element(*CheckoutPageLocators.POSTAL_CODE_INPUT_FIELD).get_attribute('value')
        assert postal_code == ReadConfig.get_valid_postal_code(), f'Postal_code не совпадают. Введено {postal_code}'

    def click_continue_button(self):
        button = self.driver.find_element(*CheckoutPageLocators.CONTINUE_BUTTON)
        button.click()

    def open_checkout_page(self):
        self.open_url(ReadConfig.get_checkout_url())