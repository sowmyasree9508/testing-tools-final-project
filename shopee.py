from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("file:///C:/Users/sowmya/Desktop/testing%20tools%20final%20project/website/sample.html")
driver.find_element_by_css_selector("a[href='./index.html']").click()
driver.find_element_by_name("username").send_keys("abcdefghi")
driver.find_element_by_name("password").send_keys("asdfghjk")
driver.find_element_by_name("submit").click()
driver.find_element_by_css_selector("a[href='./register.html']").click()
driver.find_element_by_name("First name").send_keys("abcdefghi")
driver.find_element_by_name("Last name").send_keys("abcdefghi")
driver.find_element_by_name("Email Addess").send_keys("asdfghj@gmail.com")
driver.find_element_by_name("password").send_keys("asdfghjdfg")
driver.find_element_by_name("submit").click()
driver.find_element_by_css_selector("a[href='./aboutus.html']").click()
time.sleep(2)
driver.find_element_by_css_selector("a[href='./sample.html']").click()


time.sleep(5)
driver.close()

