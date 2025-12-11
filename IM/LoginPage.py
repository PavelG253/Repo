from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    def __init__(self, driver):
        """
        Конструктор класса LoginPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step()
    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self

    @allure.step("Ввод имени пользователя для авторизации")
    def enter_username(self, username):
        """
        Ввод имени пользователя в соответствующее поле.

        :param username: str - Текст имени пользователя.
        :return: Возврат текущего экземпляра класса.
        """
        username_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_input.send_keys(username)
        return self

    @allure.step("Ввод пароля для авторизации")
    def enter_password(self, password):
        """
        Ввод пароля в соответствующее поле.

        :param password: str - Текст пароля.
        :return: Возврат текущего экземпляра класса.
        """
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(password)
        return self

    @allure.step("Переход на страницу авторизованного пользователя")
    def click_login(self):
        """
        Нажимает кнопку для перехода на страницу авторизованного пользователя.

        :return: Возвращает страницу добавления товаров в корзину.
        """
        self.driver.find_element(By.ID, "login-button").click()
        from IM.AddToCartPage import AddToCartPage
        return AddToCartPage(self.driver)
  
