from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

# Создать класс для страницы авторизации, который будет содержать методы
# для ввода логина и пароля, а также для нажатия кнопки входа.


class Autorization:
    def __init__(self, driver):
        """
        Конструктор класса Autorization.
        """
        self.driver = driver

    @allure.step("Ввод данных для авторизации")
    def input_login(self):
        """
        Осуществляет поиск и ввод в соответствующие поля {user-name},
          {password} и нажатие кнопки {login-button},
        выводит в консоль сообщение,о том что кнопка 'Login' нажата,
        ожидает загрузки страницы с товарами
        :param: driver: int - время задержки в секундах
        """
        self.driver.find_element(
            By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(
            By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(
            By.ID, "login-button").click()
        print("Кнопка 'Login' нажата")
        # Ожидание загрузки страницы с товарами
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "inventory_item")))
