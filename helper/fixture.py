import unittest
from appium import webdriver
from config import config
from helper.app import Application

class Fixture(unittest.TestCase):

    def setUp(self):
        caps = config.desired_caps
        url = config.host_url
        self.driver = webdriver.Remote(url,caps)
        self.app = Application(self.driver)

    def tearDown(self):
        self.driver.quit
