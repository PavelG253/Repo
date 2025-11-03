from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()

driver.implicitly_wait(16)

print(driver.find_element(By.CSS_SELECTOR, 'p[class="bg-success"]').text)

driver.quit()
