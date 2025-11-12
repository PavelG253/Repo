from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, first_name):
        first_name_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, "first-name"))
        )
        first_name_input.send_keys(first_name)
        return self

    def enter_last_name(self, last_name):
        last_name_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, "last-name"))
        )
        last_name_input.send_keys(last_name)
        return self

    def enter_postal_code(self, postal_code):
        postal_code_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, "postal-code"))
        )
        postal_code_input.send_keys(postal_code)
        return self

    def click_continue(self):
        self.driver.find_element(By.ID, "continue").click()
        return self

    def get_total_amount_text(self):
        total_element = self.wait.until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "summary_total_label"
            ))
        )
        return total_element.text
