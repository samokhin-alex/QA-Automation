from pages.base_page import BasePage

class LoginPage(BasePage):
    def should_be_login_link(self):
        assert self.driver.current_url == self.url, f'URL = {self.driver.current_url}, должен быть {self.url}'
