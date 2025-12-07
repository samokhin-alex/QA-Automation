from pages.base_page import BasePage
from pages.locators_page import PurchaseCompleteLocators


class PurchaseCompletePage(BasePage):
    def should_be_completed_purchase(self):
        thankyou_notification = self.driver.find_element(*PurchaseCompleteLocators.THANK_YOU_FIELD).text
        assert thankyou_notification == "Thank you for your order!", \
            f'Нет оповещения о покупке, либо оно не совпадает. На странице {thankyou_notification}'