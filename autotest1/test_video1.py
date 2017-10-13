from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("http://videojs.com/")

video=driver.find_element_by_xpath("//body/section[1]/div[1]/div[2]")

url=driver.execute_script("return arguments[0].currentSrc;", video)
print(url)

print("start")
driver.execute_script("return arguments[0].play()", video)

sleep(15)

print("stop")
driver.execute_script("arguments[0].pause()", video)

driver.quit()