from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")

search = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
search.click()

print("Кнопка была нажата, но ничего особенного не произошло")

driver.quit()
