from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    def __init__(self, driver):
        """
        Конструктор класса CheckoutPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Ввод имени")
    def enter_first_name(self, first_name):
        """
        Ввод имени в поле ввода.

        :param first_name: str -  Текст имени.
        :return: Возврат текущего экземпляра класса.
        """
        first_name_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, "first-name"))
        )
        first_name_input.send_keys(first_name)
        return self

    @allure.step("Ввод фамилии")
    def enter_last_name(self, last_name):
        """
        Ввод фамилии в поле ввода.

        :param last_name: str - Текст фамилии.
        :return: Возврат текущего экземпляра класса.
        """
        last_name_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, "last-name"))
        )
        last_name_input.send_keys(last_name)
        return self

    @allure.step("Ввод почтового кода")
    def enter_postal_code(self, postal_code):
        """
        Ввод почтового кода в поле ввода.

        :param postal_code: int - Цифры почтового кода.
        :return: Возврат текущего экземпляра класса.
        """
        postal_code_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, "postal-code"))
        )
        postal_code_input.send_keys(postal_code)
        return self

    @allure.step("Нажатие кнопки 'Продолжить'")
    def click_continue(self):
        """
        Нажимает кнопку 'продолжить'.

        :return: Возврат текущего экземпляра класса.
        """
        self.driver.find_element(By.ID, "continue").click()
        return self

    @allure.step("Получение полной суммы закааза")
    def get_total_amount_text(self):
        """
        Получает полную сумму заказа.

        :return: str — Текст результата суммы заказов.
        """
        total_element = self.wait.until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "summary_total_label"
            ))
        )
        return total_element.text
