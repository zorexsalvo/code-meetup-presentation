from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
 
# connect to google.com
driver = webdriver.Chrome(options=Options())
driver.get("https://www.google.com")
 
# find the search input field
search_field = driver.find_element(By.TAG_NAME, "input")
 
# type the search string
search_field.send_keys("CODE Co-working Space")
 
# send enter key to get the search results!
search_field.send_keys(Keys.ENTER)


driver.find_element(By.XPATH, "//a[contains(@href,'https://www.facebook.com/CODECSSH/')]").click()
