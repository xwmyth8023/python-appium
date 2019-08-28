from pages.base_page import BasePage

class MorePage(BasePage):

    my_baby_photos = "id==>'com.xogrp.thebump:id/tv_my_photo'"
    community = "id==>'com.xogrp.thebump:id/tv_community'"
    pregnancy_videos = "id==>'com.xogrp.thebump:id/tv_hbib_videos'"
    
    def click_my_baby_photos(self):
        self.click(self.my_baby_photos)
        self.sleep(2)
    
    def click_community(self):
        self.click(self.community)
        self.sleep(2)

    def click_pregnancy_videos(self):
        self.click(self.pregnancy_videos)
        self.sleep(2)