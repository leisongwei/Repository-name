#  coding:utf-8
from time import sleep
from selenium import webdriver
import unittest


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://www.zentaopm.com/user-login.html')

    def test1(self):
        self.driver.find_element_by_id('account').send_keys('qwe123456')
        self.driver.find_element_by_id('password').send_keys('123456')
        self.driver.find_element_by_id('submit').click()
        sleep(1)
        a = self.driver.find_element_by_css_selector('#siteNav>a:nth-child(1)').text
        print(a)
        self.assertEqual(a, '雷伟')

    def test2(self):
        self.driver.find_element_by_id('account').send_keys('qwe123456')
        self.driver.find_element_by_id('password').send_keys('12346')
        self.driver.find_element_by_id('submit').click()
        sleep(1)
        a = self.driver.find_element_by_css_selector('#siteNav>a:nth-child(1)').text
        print(a)
        self.assertNotEqual(a, '雷伟')

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()