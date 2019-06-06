from pages.more_page import MorePage
from pages.home_page import HomePage

class Application:
    def __init__(self, driver):
        self.more = MorePage(driver)
        self.home = HomePage(driver)