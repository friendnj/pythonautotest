from  selenium import webdriver
import  time
driver = webdriver.Firefox()
driver.get("http://m.mail.10086.cn")

print("设置浏览器宽480，高800显示")
driver.set_window_size(480,800)
time.sleep(2)
driver.set_window_size(48,80)
time.sleep(1)
driver.set_window_size(800,400)
time.sleep(1)
driver.maximize_window()

