from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def form_test():
    driver = webdriver.Edge()

    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    values_new = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in values_new.items():
        field = driver.find_element(By.NAME, field_name)
        field.send_keys(value)

    driver.find_element(By.CLASS_NAME, 'btn-outline-primary').click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, ".alert-danger")))

    zip_code_field = driver.find_element(By.ID, "zip-code")
    zip_code_classes = zip_code_field.get_attribute("class")
    assert "alert-danger" in zip_code_classes

    fields_to_check = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field_id in fields_to_check:
        field = driver.find_element(By.ID, field_id)
        field_classes = field.get_attribute("class")
        assert "alert-success" in field_classes

    driver.quit()

