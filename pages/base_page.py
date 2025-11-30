class BasePage():
    def __init__(self, driver, url):
        self.url = url
        self.driver = driver

    def open(self):
        self.driver.get(self.url)