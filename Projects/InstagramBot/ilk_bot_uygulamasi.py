from selenium import webdriver
import time
from Projects.InstagramBot.bilgiler import webdriver_path

# Create driver variable that uses Chrome
driver = webdriver.Chrome(executable_path=webdriver_path)

# Opens Chrome browser and navigates to google.com
driver.get("http://www.google.com")

# Wait two minutes
time.sleep(2)

# Close browser
driver.quit()