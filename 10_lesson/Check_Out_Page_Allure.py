from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


# Создать класс для страницы оформления заказа, который будет содержать
# методы для заполнения формы данными (имя, фамилия, почтовый индекс)
# и проверки итоговой стоимости.


class CheckoutPage:
    def __init__(self, driver):
        """
        Конструктор класса CheckoutPage.        
        """
        self.driver = driver

    @allure.step("Заполнение формы 'checkout' личными данными "
                 " и нажатие кнопки 'continue'")
    def input_info(self):
        """
        Заполняет форму 'checkout'личными данными 'first-name', 'last-name', 'post-code',
        ожидает кликабельности кнопки 'continue',
        нажимает на кнопку 'continue'
          {password} и нажатие кнопки {login-button},
        выводит в консоль сообщение,о том что кнопка 'Login' нажата,
        ожидает загрузки страницы с товарами
        :param: driver: int - время задержки в секундах
        выводит в консоль сообщение, о том что кнопка 'Сontinue' нажата,
        скроллинг страницы вверх.
        """       
        self.driver.find_element(
            By.CSS_SELECTOR, "[id='first-name']").send_keys("Владимир")

        self.driver.find_element(
            By.CSS_SELECTOR, "[id='last-name']").send_keys("Максимов")

        self.driver.find_element(
            By.CSS_SELECTOR, "[id='postal-code']").send_keys("185030")

        # Проверка кликабельности кнопки "Сontinue"
        contin = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, "[id='continue']")))
        contin = self.driver.find_element(
            By.CSS_SELECTOR, "[id='continue']")
        contin.click()
        print("Кнопка 'Continue' нажата")
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")  # пр-ка вверх

    @allure.step("Вывод в консоль итоговой стоимости заказа")
    def check_prise(self):
        """
        Выводит в консоль итоговую стоимость заказа с экрана ПК.
        :param: str - текст итоговой стоимости заказа в долларах
        """
        # Чтение итоговой стоимости        
        text_prise = self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
        text_prise_value = float(text_prise.split("$")[1])
        text_prise_value == 58.29
        text_prise = self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
        print(text_prise)

    @allure.step("Получение итоговой стоимости заказа")
    def get_total_price(self):
        """
        Возвращает итоговую стоимость заказа с экрана ПК.

        :return: float — итоговая стоимость заказа с экрана ПК в долларах.
        """
        element = self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label")
        return float(element.text.split("$")[1])
