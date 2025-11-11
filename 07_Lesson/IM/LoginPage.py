from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self

    def enter_username(self, username):
        username_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_input.send_keys(username)
        return self

    def enter_password(self, password):
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(password)
        return self

    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()
        from IM.AddToCartPage import AddToCartPage
        return AddToCartPage(self.driver)
