#  coding:utf-8
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
mouse = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text('搜索设置').click()
# sleep(3)
# driver.find_element_by_id('nr').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="nr"]/option[2]').click()
sleep(2)
driver.find_element_by_class_name('prefpanelgo').click()
sleep(1)
driver.find_element_by_class_name('prefpanelgo').click()
driver.switch_to.alert.accept()
driver.quit()