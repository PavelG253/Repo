import pytest
from selenium import webdriver
from IM.LoginPage import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


def test_shopping_cart_total(driver):
    login_page = LoginPage(driver)
    login_page.open()

    add_to_cart_page = (
        login_page
        .enter_username("standard_user")
        .enter_password("secret_sauce")
        .click_login()
    )

    add_to_cart_page \
        .add_backpack_to_cart() \
        .add_bolt_t_shirt_to_cart() \
        .add_onesie_to_cart()

    cart_page = add_to_cart_page.click_shopping_cart()
    checkout_page = cart_page.click_checkout()

    checkout_page \
        .enter_first_name("Иван") \
        .enter_last_name("Петров") \
        .enter_postal_code("123456") \
        .click_continue()

    total_text = checkout_page.get_total_amount_text()

    assert total_text == "Total: $58.29"
