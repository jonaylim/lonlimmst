from selenium import webdriver 
import time
auto = webdriver.Chrome()
auto.get("https://www.watch-movies.com.pk/category/free-indian-movies-watch/2025-movies/")
print("start the prosess")
time.sleep(50)
auto.quit()
print("worik fine! ")
