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


def login():
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys("username")
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]").clear()
    driver.find_element_by_xpath("//form/div/div[3]/div[2]/input[2]").send_keys("password")
    driver.find_element_by_id("dologin").click()


def logout():
    driver.find_element_by_link_text("退出").click()
    driver.quit()


driver = webdriver.Firefox()
driver.get("http://www.126.com")

print('Before login=============')

title = driver.title
print(title)

now_url=driver.current_url
print(now_url)
time.sleep(3)
driver.switch_to.frame("x-URS-iframe")
login()

logout()