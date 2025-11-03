from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

images = WebDriverWait(driver, timeout=15)

driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

images.until(lambda x: len(x.find_elements(By.TAG_NAME, 'img')) > 4)

source = driver.find_element(By.CSS_SELECTOR, '#award').get_attribute('src')
print(source)

driver.quit()
