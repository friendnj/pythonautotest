from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")


search_text=['zhongwen','ssss','wwww']

for text in search_text:
    driver.find_element_by_id("kw").send_keys(text)
    driver.find_element_by_id("su").click()  # 这里是因为输入完selenium之后自动搜索了，这个可能和教程不一样
    time.sleep(10)

    # js="window.scrollTo(100,500);"

    driver.quit()
