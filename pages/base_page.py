import time
from appium import webdriver
import os.path
from helper.logger import Logger
from config import config

caps = config.desired_caps
url = config.host_url

class BasePage(object):

    def __init__(self, driver):
        self.driver = webdriver.Remote(url,caps)

    def quit(self):
        self.driver.quit()

    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for {} seconds.".format(seconds))

    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with {}".format(e))

    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! {}".format(e))
            self.get_windows_img()

    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element {} successful by {} via value: {}".format(element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: {}".format(e))
                self.get_windows_img()   # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element {} successful by {} via value: {}".format(element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: {}".format(e))
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    def input(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type {} in inputBox".format(text))
        except NameError as e:
            logger.error("Failed to type in input box with {}".format(e))
            self.get_windows_img()

    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with {}".format(e))
            self.get_windows_img()

    def click(self, selector):

        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element {} was clicked.".format(text))
        except NameError as e:
            logger.error("Failed to click the element with {}".format(e))

    def get_page_title(self):
        logger.info("Current page title is {}".format(self.driver.title))
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for {} seconds".format(seconds))