from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

# Создать класс для страницы корзины, который будет содержать методы
# для нажатия кнопки Checkout и проверки содержимого корзины.


class CartPage:
    def __init__(self, driver):
        """
        Конструктор класса CartPage.        
        """
        self.driver = driver

    @allure.step("Нажатие кнопки 'checkout'")
    def click_checkout(self):
        """
        Ожидает пока кнопка 'checkout' станет кликабельной
        :param: driver: int - время задержки в секундах,
        нажимает на кнопку 'checkout',
        выводит в консоль сообщение,
          о том что кнопка 'checkout' нажата
        """        
        checkout = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "checkout")))
        checkout = self.driver.find_element(
            By.ID, "checkout")
        checkout.click()
        print("Кнопка 'Checkout' нажата")

    @allure.step("Получение списка и количества товаров в корзине")    
    def cart_contents(self):
        """
        Возвращает список и количество добавленных товаров на экран.
        :return: str — текст наименования и количества добавленных товаров.
        """
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge")
        items = self.driver.find_elements(
            By.CSS_SELECTOR, "div.cart_item_label")
        content = "\n".join([item.text for item in items])
        return content
