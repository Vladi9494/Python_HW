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
        #self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

    def input_info(self):
        self.driver.find_element(By.CSS_SELECTOR, "[id='first-name']").send_keys("Владимир")
        self.driver.find_element(By.CSS_SELECTOR, "[id='last-name']").send_keys("Максимов")
        self.driver.find_element(By.CSS_SELECTOR, "[id='postal-code']").send_keys("185030")
        self.driver.find_element(By.CSS_SELECTOR, "[id='continue']" ).click()  
        self.driver.implicitly_wait(4)

    def check_prise(self):
        result_text = self.driver_element(By.CSS_SELECTOR, "div.summary_total_label").text
        print(result_text)
        assert "$58.29" in result_text  
        self.driver.quit()          
        