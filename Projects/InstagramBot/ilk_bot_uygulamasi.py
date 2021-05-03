from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D:\Development\selenium_browser_drivers\chromedriver.exe")

driver.get("http://www.google.com")

time.sleep(2)

driver.quit()