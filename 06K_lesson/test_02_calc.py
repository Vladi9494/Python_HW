# II. Калькулятор
# Шаги:
# 1. Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java
# /slow-calculator.html в Google Chrome.
# 2. В поле ввода по локатору #delay введите значение 45.
# 3. Нажмите на кнопки:
#                       7
#                       +
#                       8
#                       =
# 4. Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.

# import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

# При обрезке и переносе длинной строки ссылки,
# на другую строку ссылка перестаёт работать ↓↓↓ (ошибка flake8)
chrome_driver_path = r"C:\Users\0\Desktop\ПИТОН_ДОМАШКИ\ДОМАШКИ_по_PYTHON\Python_HW\05_lesson\chromedriver.exe"

driver = webdriver.Chrome(service=ChromeService(chrome_driver_path))

# @pytest.fixture
# def test_calculator():
driver.maximize_window()

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

print("Сайт 'Slow calculator' открыт")
sleep(1)

fild_delay = driver.find_element(By.CSS_SELECTOR, "#delay")
fild_delay.clear()
print("Поле 'delay' найдено и очищено от предыдущих записей")
sleep(1)

fild_delay.send_keys("45")
print("B поле'delay'введено значение 45")
sleep(1)

# Определение локаторов для кнопок калькулятора:
# НАСТАВНИК!!! почему данные локаторы работают,
# но не определяются в консоли DevTools? ("is not a valid selector") ↓↓↓
# $$ ("//span[text()= '7']")
# $$ ("//*[@id='calculator']/div[2]/span[1]")
# $$ ("//*[@class='keys']/span[1]")

driver.find_element(By.XPATH, "//*[@class='keys']/span[1]").click()
sleep(1)
print("Кнопка '7' найдена и нажата")
driver.find_element(By.XPATH, "//*[@class='keys']/span[4]").click()
sleep(1)
print("Кнопка '+' найдена и нажата")
driver.find_element(By.XPATH, "//*[@class='keys']/span[2]").click()
sleep(1)
print("Кнопка '8' найдена и нажата")
driver.find_element(By.XPATH, "//*[@class='keys']/span[15]").click()
sleep(1)
print("Кнопка '=' найдена и нажата")

# $$("[class = 'screen']")
WebDriverWait(driver, 45).until(EC.text_to_be_present_in_element((
    By.CSS_SELECTOR, "[class = 'screen']"), '15'))
res = driver.find_element(By.CSS_SELECTOR, "[class = 'screen']").text
assert res == "15"
print("сумма = " + res)

driver.quit()
