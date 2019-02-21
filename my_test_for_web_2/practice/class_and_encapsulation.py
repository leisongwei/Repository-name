#  coding:utf-8
from selenium import webdriver
from practice import secondary_encapsulation


class Login():
    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver
        self.bases = secondary_encapsulation.Base(self.driver)

    def login(self, use='qwe123456', password='qwe123456'):
        self.bases.sendKeys(('id','account'),use)
        self.bases.sendKeys(('name', 'password'), password)
        self.bases.click(('id', 'submit'))
        # self.driver.find_element_by_id('account').send_keys(use)
        # self.driver.find_element_by_name('password').send_keys(password)
        # self.driver.find_element_by_id('submit').click()

    def get_login_name(self):
        try:
            a = self.driver.find_element_by_css_selector('.user-name').text
            print(a)
            return a
        except:
            a = '空'
            return a


