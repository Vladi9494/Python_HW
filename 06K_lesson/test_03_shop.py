# III. Покупка
# Шаги:
# 1. Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
# 2. Авторизуйтесь как пользователь standard_user.
# 3. Добавьте в корзину товары:
# Sauce Labs Backpack.
# Sauce Labs Bolt T-Shirt.
# Sauce Labs Onesie.
# 4. Перейдите в корзину.
# 5. Нажмите Checkout.
# 6. Заполните форму своими данными:
#                                   имя,
#                                   фамилия,
#                                   почтовый индекс.
# 7. Нажмите кнопку Continue.
# 8. Прочитайте со страницы итоговую стоимость (Total).
# 9. Закройте браузер.
# 10. Проверьте, что итоговая сумма равна $58.29.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService


def test_shop():
    # Устанавливаем и запускаем драйвер
    geckodriver_path = (r"C:\Users\0\Desktop\ПИТОН_ДОМАШКИ\ДОМАШКИ_по_PYTHON"
                        r"\Python_HW\05_lesson\geckodriver.exe")

    driver = webdriver.Firefox(service=FirefoxService(geckodriver_path))

    driver.maximize_window()

    driver.get("https://www.saucedemo.com/")
    print("Cайт 'Sause demo' открыт")

    # Авторизация
    user_name_field = driver.find_element(By.ID, "user-name")
    user_name_field.send_keys("standard_user")
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")
    print("введены данные 'tandard_user' и пароль 'standard_user'")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    print("Кнопка'Login' нажата")
    # Ожидание загрузки страницы с товарами
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

    # Добавление товаров в корзину
    add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_button.click()
    print("Выбран первый товар 'Sauce Labs Backpack'")
    add_button = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    add_button.click()
    print("Выбран второй товар 'Sauce Labs Bolt T-Shirt'")
    driver.execute_script("window.scrollTo(0, 500)")  # Прокрутка вниз
    add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    add_button.click()
    print("Выбран третий товар 'Sauce Labs Onesie'")
    # Проверка товаров корзине
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "3", "В корзине должно быть 3 товара"

    # Переход в корзину
    cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()

    # Ожидание загрузки страницы корзины
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))

    # Нажатие кнопки "Checkout"
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
    print("Кнопка 'Checkout' нажата")

    # Проверка кликабельности кнопки "Корзина"
    basket = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "a.shopping_cart_link")))
    basket = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link")
    basket.click()

    # Проверка кликабельности кнопки "Checkout"
    checkout = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "[id='checkout']")))
    checkout = driver.find_element(By.CSS_SELECTOR, "[id='checkout']")
    checkout.click()

    # Заполнение формы checkout
    first_name = driver.find_element(By.CSS_SELECTOR, "[id='first-name']")
    first_name.send_keys("Владимир")
    first_name = driver.find_element(By.CSS_SELECTOR, "[id='last-name']")
    first_name.send_keys("Максимов")
    postal_codee = driver.find_element(By.CSS_SELECTOR, "[id='postal-code']")
    postal_codee.send_keys("185030")
    print("Личные данные введены")

    # Проверка кликабельности кнопки "Сontinue"
    contin = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "[id='continue']")))
    contin = driver.find_element(By.CSS_SELECTOR, "[id='continue']")
    contin.click()
    print("Кнопка 'Continue' нажата")

    # Чтение итоговой стоимости
    text_prise = driver.find_element(
        By.CSS_SELECTOR, "div.summary_total_label").text
    text_prise_value = float(text_prise.split("$")[1])
    print(text_prise)

    driver.quit()

    # Проверка итоговой стоимости
    assert text_prise_value == 58.29
