# Общие требования:
# Создайте классы с описанием страниц.
# Каждый тест должен создавать и использовать
# необходимый объект страницы (Page).
# Каждый тест может только создавать, настраивать и закрывать драйвер.
# Остальные selenium-методы (click, send_keys, text…)
# запрещены в коде тестов (должны быть в классах страниц).
# В классах страниц не должно быть проверок.

# Автотест на калькулятор
# Цель: написать автотест для проверки функциональности калькулятора на сайте
# https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html,
# используя паттерн Page Object.
# Шаги:
# Создание класса Page Object:
# Создать класс для страницы калькулятора,
# который будет содержать методы для взаимодействия с элементами:
# Поле ввода задержки (локатор #delay).
# Кнопки калькулятора (цифры, операторы, кнопка =).
# Поле вывода результата.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 6)

    def open(self):
        self.driver.get(
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def setting_waiting(self):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    def calculator_buttons(self):
        self.driver.find_element(
            By.XPATH, "//*[@class='keys']/span[1]").click()
        self.driver.find_element(
            By.XPATH, "//*[@class='keys']/span[4]").click()
        self.driver.find_element(
            By.XPATH, "//*[@class='keys']/span[2]").click()
        self.driver.find_element(
            By.XPATH, "//*[@class='keys']/span[15]").click()
        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, "[class = 'screen']"), "15"))

    def result(self):
        res = self.driver.find_element(
            By.CSS_SELECTOR, "[class = 'screen']").text
        return res == "15"

    def close_driver(self):
        self.driver.quit()
