class Login():

    def user_login(self, driver, username,password):
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(username)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]").clear()
        driver.find_element_by_xpath("//form/div/div[3]/div[2]/input[2]").send_keys(password)
        driver.find_element_by_id("dologin").click()

    def user_logout(self,driver):
        driver.find_element_by_link_text("退出").click()
        driver.quit()

