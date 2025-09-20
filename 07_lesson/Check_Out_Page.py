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
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, "[id='continue']")))
        contin = self.driver.find_element(
            By.CSS_SELECTOR, "[id='continue']")
        contin.click()
        print("Кнопка 'Continue' нажата")
        self.driver.execute_script(
          "window.scrollTo(0, document.body.scrollHeight);")  # прокрутка вниз

    def check_prise(self):
        # Чтение итоговой стоимости        
        text_prise = self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
        text_prise_value = float(text_prise.split("$")[1])
        text_prise_value == 58.29
        text_prise = self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
        print(text_prise)

    def get_total_price(self):
        element = self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label")
        return float(element.text.split("$")[1])
