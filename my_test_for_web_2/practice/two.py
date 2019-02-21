#  coding:utf-8
from selenium.webdriver import ActionChains
from time import sleep
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('12345678')
driver.find_element_by_id('su').click()
sleep(0.5)
driver.find_element_by_xpath('//input[@id="kw"]').clear()
driver.find_element_by_xpath('//input[@id = "kw"]').send_keys('yyyyyy')
sleep(0.5)
driver.find_element_by_css_selector('#kw').clear()
driver.find_element_by_css_selector('#kw').send_keys('3242iii')
sleep(0.5)
mouse = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(mouse).perform()
sleep(1)
driver.find_element_by_link_text('搜索设置').click()
driver.quit()