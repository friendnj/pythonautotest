# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("https://www.baidu.com/")

sreach_windows=driver.current_window_handle

time.sleep(1)
driver.find_element_by_link_text('学术').click()
#driver.find_element_by_class_name('lb').click()
driver.find_element_by_id('lb').click()
#driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()

all_handles=driver.window_handles

for handle in all_handles:
    if handle !=sreach_windows:
        driver.switch_to.window(handle)
        print('now register window!')
        driver.find_element_by_name("userName").send_keys('seletest')
        driver.find_element_by_name('phone').send_keys('11111')
        time.sleep(2)

for handle in all_handles:
    if handle==sreach_windows:
        driver.switch_to.window(handle)
        print('now sreach window!')
        driver.find_element_by_id('TANGRAM_PSP_2_closeBtn').click()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(2)

