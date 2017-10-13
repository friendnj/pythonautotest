from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
time.sleep(2)
driver.find_element_by_id("kw").send_keys("seleniumm")
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.SPACE)

driver.find_element_by_id("kw").send_keys(Keys.SPACE)
time.sleep(2)
driver.find_element_by_id("kw").send_keys("教程")
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
time.sleep(2)
driver.find_element_by_id("su").send_keys(Keys.ENTER)