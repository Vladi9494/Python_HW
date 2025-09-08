# I Форма
# Шаги:
# 1. Откройте страницу: https://bonigarcia.dev
# /selenium-webdriver-java/data-types.html в Edge или Safari.
# 2. Заполните форму значениями:
# First name    Иван
# Last name     Петров
# Address       Ленина, 55-3
# Email         test@skypro.com
# Phone number  +7985899998787
# Zip code      *оставить пустым
# City          Москва
# Country       Россия
# Job position  QA
# Company       SkyPro

# 3. Нажмите кнопку Submit.
# 4. Проверьте (assert), что поле Zip code подсвечено красным.
# 5. Проверьте (assert), что остальные поля подсвечены зеленым.

# import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException

# При обрезке и переносе длинной строки ссылки,
# на другую строку ссылка перестаёт работать ↓↓↓ (ошибка flake8)
edge_driver_path = r"C:\Users\0\Desktop\ПИТОН_ДОМАШКИ\ДОМАШКИ_по_PYTHON\Python_HW\05_lesson\msedgedriver.exe"

driver = webdriver.Edge(service=EdgeService(edge_driver_path))

driver.maximize_window()

# @pytest.fixture
# def test_data_types():

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
print("Сайт открыт")

search_input = driver.find_element(By.NAME, "first-name")
search_input.send_keys("Иван")

search_input = driver.find_element(By.NAME, "last-name")
search_input.send_keys("Петров")

search_input = driver.find_element(By.NAME, "address")
search_input.send_keys("Ленина, 55-3")

search_input = driver.find_element(By.NAME, "zip-code")

search_input = driver.find_element(By.NAME, "city")
search_input.send_keys("Москва")
search_input = driver.find_element(By.NAME, "country")
search_input.send_keys("Россия")

search_input = driver.find_element(By.NAME, "e-mail")
search_input.send_keys("test@skypro.com")

search_input = driver.find_element(By.NAME, "phone")
search_input.send_keys("+7985899998787")

search_input = driver.find_element(By.NAME, "job-position")
search_input.send_keys("QA")

search_input = driver.find_element(By.NAME, "company")
search_input.send_keys("SkyPro")

sleep(2)
#  ↑↑↑ К сожалению скрипт стабильно работает без ошибок,
#  только со sleep (1-2 сек) в даном месте
#  Сложилось впечатление, что явное ожидание совсем
#  не работает и ни как не помогает?

# company = WebDriverWait(driver, 20).until(
# EC.visibility_of_element_located((By.NAME, "company"))).send_keys("SkyPro")

print("Поля заполнены")

# Проверка кликабельности кнопки "Submit"
button = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((
    By.CSS_SELECTOR, "button[class='btn btn-outline-primary mt-3']")))

button = driver.find_element(
    By.CSS_SELECTOR, "button[class='btn btn-outline-primary mt-3']")
button.click()

print('Кнопка "Submit" найдена')
print("Кнопка 'Submit' нажата")
print("Страница с подсветкой полей открыта")

# Определение локаторов
# $$("#zip-code")
# $$(".alert-danger")красное поле
# $$(".alert.py-2.alert-danger")
# $$(".alert.py-2")
# $$(".alert-success") зелёное поле
# $$(".alert.py-2.alert-success")

zip_fild = driver.find_element(By.ID, "zip-code")
zip_color = zip_fild.value_of_css_property("border-color")
assert zip_color == "rgb(245, 194, 199)"

zip_fields = ["first-name", "last-name", "address", "e-mail", "phone",
              "city", "country", "job-position", "company"]
for zip_field in zip_fields:
    zip_fields = driver.find_element(
      By.CSS_SELECTOR, ".alert-success").value_of_css_property("border-color")
    assert zip_fields == "rgb(186, 219, 204)"
driver.quit()

# Наставник!!! Почему при выборе другого значения цвета (color:#842029;
# background-color:#f8d7da;background-color: rgb(209, 231, 221))
# при проверке assert выпадает ошибка? Данные вводятся соответственно
# для поля и цвета правильные, но они НЕ РАБОТАЮТ? Это баг?
