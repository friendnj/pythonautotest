from selenium import webdriver
driver = webdriver.Firefox()

driver.get("https://mail.qq.com/")
driver.switch_to.frame("login_frame")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/a[2]").click()
driver.find_element_by_id("u").clear()
driver.find_element_by_id("u").clear()
driver.find_element_by_xpath("html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input").send_keys("username")
driver.find_element_by_xpath("html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]").clear()
driver.find_element_by_xpath("html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]").send_keys("password")
driver.find_element_by_id("dologin").click()