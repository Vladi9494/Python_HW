from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest
from selenium import webdriver
from AutorizationAllure import Autorization
from MainPageAllure import MainPage
from CartPageAllure import CartPage
from Check_Out_Page_Allure import CheckoutPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации, открытия сайта магазина и завершения работы драйвера.
    """
    geckodriver_path = (r"C:\Users\0\Desktop\ПИТОН_ДОМАШКИ\ДОМАШКИ_по_PYTHON"
                        r"\Python_HW\05_lesson\geckodriver.exe")
    driver = webdriver.Firefox(service=FirefoxService(geckodriver_path))
    # Открыть сайт магазина
    driver.implicitly_wait(6)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

@allure.title("Тестирование сайта магазина")
@allure.description("Тест проверяет корректность работы сайта магазина "
                    "с различными операциями по заказу товаров.")
@allure.feature("Сайт магазина")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_flow(driver):
    auth_page = Autorization(driver)
    with allure.step("Ввод данных для авторизации ('user-name'"
                     " 'password' и  нажатие кнопки 'login')"):
        auth_page.input_login()
    
    main_page = MainPage(driver)
    with allure.step("Добавление товаров в корзину"):   
        main_page.add_to_cart()
    
    with allure.step("Проверка товаров в корзине"):
        cart_badge = main_page.cart_badge()
        assert cart_badge == "3", "В корзине должно быть 3 товара"
    
    with allure.step("Переход в корзину"):
        main_page.go_to_cart()
        
    cart = CartPage(driver)
    with allure.step("Нажать на кнопку 'checkout'"):
        cart.click_checkout()
    
    personal_data = CheckoutPage(driver)
    with allure.step("Заполнение формы (оформления заказа)"
    " 'checkout' личными данными: Имя, Фамилия, Почтовый индекс"):
        personal_data.input_info()
        personal_data.check_prise()
    
    checkout_page = CheckoutPage(driver)
    with allure.step("Чтение со страницы итоговой стоимости заказа (total_price)"):
        total_price = checkout_page.get_total_price()
    driver.quit()

    with allure.step("Проверка итоговой стоимости"):
        assert total_price == 58.29
