import pytest
from selenium import webdriver
from Calculator.CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    calculator = CalculatorPage(driver)

    calculator.open()

    calculator.set_delay(45)

    calculator.perform_calculation('7', '+', '8')

    result = calculator.get_result()
    assert result == "15", f"Ожидался результат 15, но получено {result}"

