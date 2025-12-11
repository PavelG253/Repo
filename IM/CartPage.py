from selenium.webdriver.common.by import By
import allure


class CartPage:
    def __init__(self, driver):
        """
        Конструктор класса CartPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Переход в корзину")
    def click_checkout(self):
        """
        Переход в корзину по id.

        :return: Возвращает страницу оформления заказа.
        """
        self.driver.find_element(By.ID, "checkout").click()
        from IM.CheckoutPage import CheckoutPage
        return CheckoutPage(self.driver)
