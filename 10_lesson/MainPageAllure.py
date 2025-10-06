from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    def __init__(self, driver):
        """
        Конструктор класса MainPage.
        """
        self._driver = driver

    @allure.step("Поочерёдный поиск и добавление товаров в корзину")
    def add_to_cart(self):
        """
        Ожидает пока кнопка выбора первого товара станет кликабельной
        :param: driver: int - время задержки в секундах,
        осуществляет поочерёдный поиск и добавление товаров в корзину,
        с прокруткой страницы вниз и вверх
        :param: int расстояние прокрутки в пикселях
        """
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

    @allure.step("Получение списка и"
                 " количества добавленных товаров в корзину")
    def cart_badge(self):
        """
        Возвращает список и количество добавленных товаров на экран.
        :return: str — текст наименования и количества добавленных товаров.
        """
        cart_badge = self._driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge")
        return cart_badge.text

    @allure.step("Ожидание кликабельности и нажатия кнопки корзины,"
                 "и ожидание загрузки страницы корзины")
    def go_to_cart(self):
        """
        Ожидает пока кнопка корзины станет кликабельной
        :param: _driver: int время задержки в секундах,
        поиск и нажатие на значок изображения корзины,
        выводит в консоль сообщение, о том что кнопка корзины нажата,
        ожиданиет загрузки страницы корзины,
        :param: _driver: int время задержки в секундах
        скроллинг страницы вниз.
        """
        basket = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, "a.shopping_cart_link")))
        basket = self._driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link")
        basket.click()
        print("Кнопка 'Корзина' нажата")
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
        self._driver.execute_script(
          "window.scrollTo(0, document.body.scrollHeight);")  # прокрутка вниз
