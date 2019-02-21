import time
import unittest
from selenium import webdriver
from practice.class_and_encapsulation import Login
from practice import secondary_encapsulation


class AddBug(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://rrrrrrrqwe.zentaopm.com/user-login-Lw==.html')
        cls.base = secondary_encapsulation.Base(cls.driver)
        cls.loginer = Login(cls.driver)
        cls.loginer.login('qwe123456', 'qwe123456')

    def test1(self):
        loc_test1 = ('xpath', "//*[@class='nav nav-default']/li[@data-id='qa']/a")
        self.base.click(loc_test1)
        loc_bug1 = ('xpath', "//li[@data-id='bug']/a")
        self.base.click(loc_bug1)
        loc_push_bug1 = ('xpath', "//div/a[4]/i[@class='icon icon-plus']")
        self.base.click(loc_push_bug1)
        loc_version = ('xpath', "//div[@id='openedBuild_chosen']/ul[@class='chosen-choices']")
        self.base.click(loc_version)
        loc_version_choose = ('xpath', '//ul[@class="chosen-results"]/li')
        self.base.click(loc_version_choose)
        loc_title = ('id', 'title')
        text = 'bug' + time.asctime()
        self.base.sendKeys(loc_title,text)
        self.driver.switch_to.frame(1)
        loc_content = ('xpath', '/html/body/p[1]')
        self.base.sendKeys(loc_content, '222222222')
        self.driver.switch_to.default_content()
        loc_save = ('id', 'submit')
        self.base.click(loc_save)