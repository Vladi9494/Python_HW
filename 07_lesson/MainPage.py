from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Создать класс для главной страницы магазина, который будет содержать
# методы для добавления товаров в корзину и перехода в корзину.
class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/inventory.html")

    # добавление товаров в корзину
    def add_to_cart(self):
        add_button = self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        #add_button = self._driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
        add_button.click()
        add_button = self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        add_button = self._driver.execute_script("window.scrollTo(0, 500)") # прокрутка вниз
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    
    sleep(6)
    # переход в корзину
    def go_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, "button[class='btn btn_primary btn_small btn_inventory ']").click()

    # ожидание загрузки страницы корзины
   