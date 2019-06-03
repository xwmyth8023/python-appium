from base_page import BasePage

class MorePage(BasePage):

    more = "id==>'com.xogrp.thebump:id/more'"

    def click_more(self):
        self.click(self.more)
        self.sleep(2)