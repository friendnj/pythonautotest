from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.126.com")

print('Before login=============')

title = driver.title
print(title)

now_url=driver.current_url
print(now_url)
time.sleep(3)
driver.switch_to.frame("x-URS-iframe")


p