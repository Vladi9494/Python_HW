from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создать класс для страницы корзины, который будет содержать методы
# для нажатия кнопки Checkout и проверки содержимого корзины.


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    # нажатие кнопки "Checkout"
    def click_checkout(self):
        # Проверка кликабельности кнопки "Checkout"
        checkout = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "checkout")))
        checkout = self.driver.find_element(
            By.ID, "checkout")
        checkout.click()
        print("Кнопка 'Checkout' нажата")

        # проверка содержимого корзины
    def cart_contents(self):
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge")
        items = self.driver.find_elements(
            By.CSS_SELECTOR, "div.cart_item_label")
        content = "\n".join([item.text for item in items])
        return content
