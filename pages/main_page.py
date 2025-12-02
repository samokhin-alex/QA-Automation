from pages.base_page import BasePage
from .locators_page import MainPageLocators


class MainPage(BasePage):

    def should_be_inventory_list(self):
        assert self.is_element_visible(MainPageLocators.INVENTORY_LIST)