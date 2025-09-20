# Автотест на интернет-магазин
# Цель: написать автотест для проверки функциональности
# интернет-магазина на сайте https://www.saucedemo.com/,
# используя паттерн Page Object.
# Шаги:
# Создание класса Page Object:

# Создать класс для страницы авторизации, который будет содержать методы
# для ввода логина и пароля, а также для нажатия кнопки входа.

# Создать класс для главной страницы магазина, который будет содержать
# методы для добавления товаров в корзину и перехода в корзину.

# Создать класс для страницы корзины, который будет содержать методы
# для нажатия кнопки Checkout и проверки содержимого корзины.

# Создать класс для страницы оформления заказа, который будет содержать
# методы для заполнения формы данными (имя, фамилия, почтовый индекс)
# и проверки итоговой стоимости.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создать класс для страницы оформления заказа, который будет содержать
# методы для заполнения формы данными (имя, фамилия, почтовый индекс)
# и проверки итоговой стоимости.
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def input_info(self):
        # Заполнение формы checkout своими данными
        self.driver.find_element(
            By.CSS_SELECTOR, "[id='first-name']").send_keys("Владимир")

        self.driver.find_element(
            By.CSS_SELECTOR, "[id='last-name']").send_keys("Максимов")

        self.driver.find_element(
            By.CSS_SELECTOR, "[id='postal-code']").send_keys("185030")

        # Проверка кликабельности кнопки "Сontinue"
        contin = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='continue']")))
        contin = self.driver.find_element(By.CSS_SELECTOR, "[id='continue']")
        contin.click()
        print("Кнопка 'Continue' нажата")
        self.driver.execute_script(
          "window.scrollTo(0, document.body.scrollHeight);")  # прокрутка вниз

    def check_prise(self):
        # Чтение итоговой стоимости
        text_prise = self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
        print(text_prise)
