
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get("http://www.youtube.com")
# time(10)
inputFindElement = driver.find_element(By.NAME, "search_query")
inputFindElement.clear()
inputFindElement.send_keys("string_to_search")
searchButton = driver.find_element(By.ID, "search-icon-legacy")
searchButton.click()
time.sleep(3)
startTheVideoButton = driver.find_element(By.XPATH, "(//*[@id='thumbnail']/yt-image/img)[47]")
startTheVideoButton.click()
stopTheVideoButton = driver.find_element(By.XPATH, "//*[@id='movie_player']/div[35]/div[2]/div[1]/button")
stopTheVideoButton.click()