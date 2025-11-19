from selenium.webdriver.common.by import By


class AddToCartPage:
    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()
        return self

    def add_bolt_t_shirt_to_cart(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        return self

    def add_onesie_to_cart(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()
        return self

    def click_shopping_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        from IM.CartPage import CartPage
        return CartPage(self.driver)
