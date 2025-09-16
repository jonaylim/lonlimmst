from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.watch-movies.com.pk/category/free-indian-movies-watch/2025-movies/")
print("Program starts...")
time.sleep(3) 
driver.quit()
print("work fine!")