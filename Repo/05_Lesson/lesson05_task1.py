from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")

search = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
search.click()

driver.quit()
