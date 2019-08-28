from helper.fixture import Fixture
import unittest
import time

class More_Page_Test(Fixture):

    def test_more(self):
        self.app.home.go_to_more()
        self.app.more.click_community()