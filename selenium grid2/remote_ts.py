from selenium import webdriver

driver=webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
              desired_capabilities={'platform':'ANY',
                                    'browserName':'firefox',
                                    'version':'',
                                    'javascriptEnabled':True
                                    }
              )

driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys("remote")
driver.find_element_by_id("su").click()