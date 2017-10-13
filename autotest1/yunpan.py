from selenium import webdriver
from  selenium.webdriver.common.action_chains import ActionChains
import time


driver=webdriver.Firefox()
driver.get("https://www.baidu.com")

above=driver.find_element_by_name("tj_settingicon")
ActionChains(driver).move_to_element(above).perform()

