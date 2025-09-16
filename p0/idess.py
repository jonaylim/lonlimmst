from selenium import webdriver 
import time
from  selenium.webdriver.common.by import By
auto = webdriver.Chrome()
auto.maximize_window()
auto.get("https://www.watch-movies.com.pk/")
time.sleep(8)
s = auto.find_element(By.ID,value="s")
s.send_keys("black")
auto.minimize_window()
time.sleep(7)

print("s")

