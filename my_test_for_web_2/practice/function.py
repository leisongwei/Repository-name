
def login(driver, use='qwe123456', password='qwe123456'):
    driver.find_element_by_id('account').send_keys(use)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_id('submit').click()