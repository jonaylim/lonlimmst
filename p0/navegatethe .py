from selenium import webdriver 
import time 
auto = webdriver.Chrome()
auto.get("https://www.watch-movies.com.pk/")
auto.refresh()
time.sleep(20)
auto.forward()
auto.get("https://www.watch-movies.com.pk/category/free-indian-movies-watch/2025-movies/")
auto.refresh()
time.sleep(15)
auto.back()
time.sleep(7)
auto.quit()
print("work fine!")