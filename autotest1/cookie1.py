from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://www.youdao.com")

driver.add_cookie({'name':'key-aaaaa','value':'value-bbbbb'})
for cookie in driver.get_cookies():
    print("%s->%s"%(cookie['name'],cookie['value']))

driver.quit()

