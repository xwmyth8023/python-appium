from appium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import  expected_conditions as EC

import unittest

import time

from time import sleep

import desired_capabilities



class AndroidTest(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        desired_cap = desired_capabilities.get_desired_capabilities()

        uri = desired_capabilities.get_uri()

        self.driver = webdriver.Remote(uri,desired_cap)

        time.sleep(3)


    @classmethod
    def tearDownClass(self):
        self.driver.quit()


    def leftSwipe(self):
        window_size = self.driver.get_window_size()
        self.driver.swipe(start_x=window_size["width"] * 0.8,
                          start_y=window_size["height"] * 0.5,
                          end_x=window_size["width"] * 0.1,
                          end_y=window_size["height"] * 0.5 )


    def test_a_utFrame(self):
        time.sleep(3)
        print(self.driver.current_activity)
        # create_btn = self.driver.find_element_by_id("com.xogrp.thebump:id/bt_create_user")
        log_btn = self.driver.find_element_by_id("com.xogrp.thebump:id/bt_login_tb")
        log_btn.click()
        time.sleep(3)
        email_input = self.driver.find_element_by_id("com.xogrp.thebump:id/et_email_address")
        email_input.send_keys('appium@app.com')
        passwrod_input = self.driver.find_element_by_id("com.xogrp.thebump:id/et_password")
        passwrod_input.send_keys('123456')
        login_btn = self.driver.find_element_by_id("com.xogrp.thebump:id/tv_login")
        login_btn.click()
        time.sleep(3)
        welcome = self.driver.find_element_by_id("com.xogrp.thebump:id/tv_welcomeback")
        welcomeDescription = self.driver.find_element_by_id("com.xogrp.thebump:id/tv_updatestatus_content")
        update_status = self.driver.find_element_by_id("com.xogrp.thebump:id/tv_removestatus_nostatus")

        self.assertEqual(welcome.text,'WELCOME')
        self.assertEqual(welcomeDescription.text,"Welcome back to The Bump. Whenever you're ready, you can update your status.")
        self.assertEqual(update_status.text,'UPDATE MY STATUS')

        time.sleep(2)

if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(AndroidTest("test_a_utFrame"))
    unittest.TextTestRunner(verbosity=2).run(suite)