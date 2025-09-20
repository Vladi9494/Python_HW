from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest
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


def test_shop_flow(driver):
    auth_page = Autorization(driver)
    auth_page.input_login()
    # Добавление в корзину товаров
    main_page = MainPage(driver)
    main_page.add_to_cart()
    # Проверка товаров в корзине
    cart_badge = driver.find_element(
        By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "3", "В корзине должно быть 3 товара"
    # Переход в корзину
    main_page.go_to_cart()
    # Нажать кнопку Checkout
    cart = CartPage(driver)
    cart.click_checkout()
    # Заполненение формы своими данными
    # (Имя, Фамилия, Почтовый индекс)
    personal_data = CheckoutPage(driver)
    personal_data.input_info()
    personal_data.check_prise()
    # Прочитать со страницы итоговую стоимость (Total)
    checkout_page = CheckoutPage(driver)
    total_price = checkout_page.get_total_price()
    driver.quit()
    assert total_price == 58.29
