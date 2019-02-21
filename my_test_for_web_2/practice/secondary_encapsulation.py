#  coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def find_element(self, locator):
        ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        return ele

    def sendKeys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def click(self, locator):
        self.find_element(locator).click()

    def scroll(self, locator):
        ele = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('http://gz.ganji.com/')
    base = Base(driver)
    loc = ('xpath', '//*[text()="靠谱放心车"]')
    base.scroll(loc)
    # loc1 = ('id', 'account')
    # loc2 = ('css selector', '[name = "password"]')
    # loc3 = ('xpath', '//*[@id = "submit"]')
    # base.sendKeys(loc1,'qwe123456')
    # base.sendKeys(loc2, 'qwe123456')
    # base.click(loc3)
