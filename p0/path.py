from selenium import  webdriver
import time
from selenium.webdriver.common.by import By
auto = webdriver.Edge()
auto.get('https://www.watch-movies.com.pk/')
time.sleep(3)
auto.maximize_window()
s = auto.find_element(By.ID,value='s')
s.send_keys("black")
time.sleep(4)
btn = auto.find_element(By.XPATH,value='//input[@type="submit"]')
time.sleep(4)
btn.click()
input("Press Enter to quit...")
auto.quit()

