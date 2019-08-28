from pages.base_page import BasePage

class HomePage(BasePage):

    avatar = "id==>'com.xogrp.thebump:id/iv_avatar'"
    bump_logo = "id==>'com.xogrp.thebump:id/iv_bump_logo_title'"
    explore = "id==>'com.xogrp.thebump:id/rl_context_menu'"
    more = "id==>'com.xogrp.thebump:id/more'"

    def go_to_profile(self):
        self.click(self.avatar)
        return self

    def go_to_explore(self):
        self.click(self.explore)
        return self

    def go_to_more(self):
        self.click(self.more)
        return self
