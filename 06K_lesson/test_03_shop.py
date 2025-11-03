from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shopping_cart_total():
    driver = webdriver.Firefox()

    driver.get("https://www.saucedemo.com/")

    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack").click()

    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()

    first_name_input = driver.find_element(By.ID, "first-name")
    first_name_input.send_keys("Иван")

    last_name_input = driver.find_element(By.ID, "last-name")
    last_name_input.send_keys("Петров")

    postal_code_input = driver.find_element(By.ID, "postal-code")
    postal_code_input.send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    wait = WebDriverWait(driver, 10)
    total_element = wait.until(EC.presence_of_element_located((
        By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text

    assert total_text == "Total: $58.29"

    driver.quit()
