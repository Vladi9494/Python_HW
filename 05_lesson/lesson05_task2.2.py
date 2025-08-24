# Упражнение 2. Клик по кнопке без ID
# Создайте скрипт lesson05_task2.py.
# Открыть браузер Google Chrome.(Firefox)
# Перейти на страницу: http://uitestingplayground.com/dynamicid.
# Кликнуть на синюю кнопку.
# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options

# Устанавливаем и запускаем драйвер
service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("http://uitestingplayground.com/dynamicid")
sleep(2)
# class = "btn btn-primary"
blue_button = driver.find_element(
    By.CSS_SELECTOR, "button[class='btn btn-primary']")
blue_button.click()
# ИЛИ ↓↓↓
# search_box = driver.find_element(
# By.XPATH, "//button[contains(text(), 'Button with Dynamic ID')]").click()

sleep(5)
driver.quit()
