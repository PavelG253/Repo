from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")

search = driver.find_element(By.CSS_SELECTOR, "#username")

search.send_keys("tomsmith")

search = driver.find_element(By.CSS_SELECTOR, "#password")

search.send_keys("SuperSecretPassword!", Keys.ENTER)

sleep(1)

element = (driver.find_element(By.CSS_SELECTOR, "#flash").text)
print(element)

driver.quit()
