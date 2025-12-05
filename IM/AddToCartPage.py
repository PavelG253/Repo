from selenium.webdriver.common.by import By
import allure


class AddToCartPage:
    def __init__(self, driver):
        """
        Конструктор класса AddToCartPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Добавление элемента 'рюкзак' в корзину")
    def add_backpack_to_cart(self):
        """
        Добавление элемента в корзину по id.

        :return: Возврат текущего экземпляра класса.
        """
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()
        return self

    @allure.step("Добавление элемента 'футболка' в корзину")
    def add_bolt_t_shirt_to_cart(self):
        """
        Добавление элемента в корзину по id.

        :return: Возврат текущего экземпляра класса.
        """
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        return self

    @allure.step("Добавление элемента 'онезия' в корзину")
    def add_onesie_to_cart(self):
        """
        Добавление элемента в корзину по id.

        :return: Возврат текущего экземпляра класса.
        """
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()
        return self

    @allure.step("Переход в корзину")
    def click_shopping_cart(self):
        """
        Docstring for click_shopping_cart

        :return: Возвращает страницу корзины.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        from IM.CartPage import CartPage
        return CartPage(self.driver)
