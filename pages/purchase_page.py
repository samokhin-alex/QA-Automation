from selenium.webdriver.common.by import By
from pages.locators_page import PurchasePageLocators, MainPageLocators
from pages.main_page import MainPage


class PurchasePage(MainPage):

    def should_be_correct_price(self):
        purchase_items = self.driver.find_elements(*PurchasePageLocators.PURCHASE_ITEMS)
        purchase_item_price = purchase_items[0].find_element(By.CSS_SELECTOR, '[class="inventory_item_price"]').text
        assert purchase_item_price == MainPage.get_1_price(self), \
            f'Цены в каталоге и в покупке не совпадают. В каталоге {MainPage.get_1_price(self)}, а в покупке {purchase_item_price}'

    def get_sum_price(self):
        element = self.driver.find_element(*PurchasePageLocators.SUBTOTAL_PRICE)

        price_text = self.driver.execute_script("""
                return arguments[0].childNodes[1].textContent;
            """, element)

        return float(price_text.strip())

    def get_calculated_tax(self):
        calculated_tax = round(self.get_sum_price() * 0.08, 2)
        return calculated_tax

    def should_be_correct_tax(self):
        tax_element = self.driver.find_element(*PurchasePageLocators.TAX)

        # Аналогично для налога
        tax_text = self.driver.execute_script("""
                return arguments[0].childNodes[1].textContent;
            """, tax_element)

        tax_on_page = float(tax_text.strip())
        calculated_tax = self.get_calculated_tax()

        assert abs(tax_on_page - calculated_tax) < 0.01, \
            f'Значения tax не совпадают. Расчетная tax = ${calculated_tax:.2f}, а на странице покупки ${tax_on_page:.2f}'

    def click_finish_button(self):
        button =self.driver.find_element(*PurchasePageLocators.FINISH_BUTTON)
        button.click()