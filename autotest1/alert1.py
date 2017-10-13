from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
link=driver.find_element_by_link_text('学术').click()
link=driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()

driver.find_element_by_link_text("搜索设置").click()

driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(4)

driver.switch_to.alert().accept()




