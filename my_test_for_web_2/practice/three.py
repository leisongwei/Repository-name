#  coding:utf-8
# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.get('http://mail.126.com/')
# driver.switch_to.frame(2)
# driver.find_element_by_name('email').send_keys('123')
# driver.quit()
# driver.switch_to.default_content()
# driver.switch_to.parent_frame()


from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://bj.ganji.com/')
print(driver.title)
driver.find_element_by_link_text('房东直租').click()
driver.close()
handle = driver.window_handles
driver.switch_to.window(handle[-1])
print(driver.title)
