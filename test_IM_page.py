import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from IM.LoginPage import LoginPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера в режиме инкогнито.
    """
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


@allure.title("Тестирование функциональности интернет магазина")
@allure.description("Тест проверяет корректность добавления товаров в ИМ и "
                    "сравнение заданной и полученной сумм в корзине")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shopping_cart_total(driver):
    """
    Тест проверяет корректность добавления товаров в ИМ и
    сравнение заданной и полученной сумм в корзине
    """
    with allure.step("Открытие страницы авторизации"):
        login_page = LoginPage(driver)
        login_page.open()

    with allure.step("Ввод данных для авторизации"):
        add_to_cart_page = (
            login_page
            .enter_username("standard_user")
            .enter_password("secret_sauce")
            .click_login()
        )

    with allure.step("Добавление рюкзака в корзину"):
        add_to_cart_page.add_backpack_to_cart()
    with allure.step("Добавление футболки в корзину"):
        add_to_cart_page.add_bolt_t_shirt_to_cart()
    with allure.step("Добавление онезии в корзину"):
        add_to_cart_page.add_onesie_to_cart()

    with allure.step("Переход в корзину"):
        cart_page = add_to_cart_page.click_shopping_cart()
    with allure.step("Переход к оформлению заказа"):
        checkout_page = cart_page.click_checkout()

    with allure.step("Заполнение информации о покупателе"):
        checkout_page \
            .enter_first_name("Иван") \
            .enter_last_name("Петров") \
            .enter_postal_code("123456") \
            .click_continue()
    with allure.step("Получение общей суммы стоимости товаров в корзине"):
        total_text = checkout_page.get_total_amount_text()
    with allure.step("Проверка соответствия заданной и полученной сумм товаров"
                     " в корзине"):
        assert total_text == "Total: $58.29"
