#  coding:utf-8
from time import sleep
from selenium import webdriver
import unittest
from practice.class_and_encapsulation import Login
import ddt


data111 = [{'use': 'qwe123456','password': 'qwe123456'},{'use': 'qwe123456','password': 'qwe123456'}, {'use': 'qwe123456','password': 'qwe123456'}]

@ddt.ddt
class Login_chandao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginer = Login(cls.driver)
        cls.driver.get('https://rrrrrrrqwe.zentaopm.com/user-login-Lw==.html')

    @ddt.data(*data111)
    def test1(self, data1):
        self.loginer.login(data1['use'],data1['password'])
        sleep(1)
        a = self.loginer.get_login_name()
        self.assertEqual(a, 'qwe123456')

    def test2(self):
        self.loginer.login('qwe12356', 'qwe123456')
        sleep(1)
        a = self.loginer.get_login_name()
        self.assertNotEqual(a, 'qwe123456')

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()