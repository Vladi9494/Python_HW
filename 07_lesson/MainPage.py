from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создать класс для главной страницы магазина, который будет содержать
# методы для добавления товаров в корзину и перехода в корзину.


class MainPage:
    def __init__(self, driver):
        self._driver = driver

    # добавление товаров в корзину
    def add_to_cart(self):
        # Ждем пока кнопка станет кликабельной
        button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((
                By.ID, "add-to-cart-sauce-labs-backpack")))
        button.click()
        button = self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        button = self._driver.execute_script(
            "window.scrollTo(0, 500)")  # прокрутка вниз
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()
        button = self._driver.execute_script(
            "window.scrollTo(500, 0)")  # прокрутка вверх

    def cart_badge(self):
        cart_badge = self._driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge")
        return cart_badge.text

    def go_to_cart(self):
        # Проверка кликабельности кнопки "Корзина"
        basket = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, "a.shopping_cart_link")))
        basket = self._driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link")
        basket.click()
        print("Кнопка 'Корзина' нажата")
        # ожидание загрузки страницы корзины
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
        self._driver.execute_script(
          "window.scrollTo(0, document.body.scrollHeight);")  # прокрутка вниз
