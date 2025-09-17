# Создание теста:
# Написать тест, который использует PageObject
# для выполнения следующих действий:
# Открыть сайт магазина.
# Авторизоваться как пользователь standard_user.
# Добавить в корзину товары:
# Sauce Labs Backpack.
# Sauce Labs Bolt T-Shirt.
# Sauce Labs Onesie.
# Перейти в корзину.
# Нажать кнопку Checkout.
# Заполнить форму своими данными:
# Имя.
# Фамилия.
# Почтовый индекс.
# Прочитать со страницы итоговую стоимость (Total).
# Закрыть браузер.
# Проверить (assert), что итоговая сумма равна $58.29.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest
from time import sleep
from selenium import webdriver
from Autorization import Autorization
from MainPage import MainPage
from CartPage import CartPage
from Check_Out_Page import CheckoutPage

@pytest.fixture
def driver():
    geckodriver_path = (r"C:\Users\0\Desktop\ПИТОН_ДОМАШКИ\ДОМАШКИ_по_PYTHON"
                        r"\Python_HW\05_lesson\geckodriver.exe")
    driver = webdriver.Firefox(service=FirefoxService(geckodriver_path))
    # Открыть сайт магазина
    driver.implicitly_wait(6)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

    sleep(5)
    # Авторизоваться как пользователь standard_user.
def test_autorization(driver):
    auth_page = Autorization(driver)
    auth_page.input_login()
    # Ожидание загрузки страницы с товарами
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    sleep(5)
    # Добавление в корзину товаров
def test_main_page(driver):
    main_page = MainPage(driver)
    main_page.add_to_cart()
    # Переход в корзину
    main_page.go_to_cart()
    # Ожидание загрузки страницы корзины
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
    sleep(4)    
#     # Нажать кнопку Checkout
# def test_cart_page(driver):
#     cart = CartPage(driver)
#     cart.click_checkout() 
#     cart.cart_contents()
#     actual_content = cart.cart_contents()
#     expected_content = "Sauce Labs Backpack\nSauce Labs Bolt T-Shirt\nSauce Labs Onesie"    
#     assert actual_content == expected_content
 
# cart_content = cart_page.get_cart_content()
# assert cart_content == "Ожидаемое содержание"


       # Заполненение формы своими данными (Имя, Фамилия, Почтовый индекс)
# def test_check_out_page(driver):
#     personal_data = CheckoutPage(browser)
#     personal_data.input_info() 
#     personal_data.check_prise()   

   
    # Прочитать со страницы итоговую стоимость (Total)
    # total_price = buy.check_cost()
    # expected = "Total: $58.29"
    # assert expected == "total_price"

    # Закрыть браузер
    # self.driver.quit()
    # Проверить (assert), что итоговая сумма равна $58.29.


