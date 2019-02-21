from time import sleep
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.get('https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh#en/zh/')
driver.back()
driver.forward()
driver.refresh()
sleep(2)
driver.close()
driver.quit()