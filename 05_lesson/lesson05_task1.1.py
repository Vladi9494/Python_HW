# Упражнение 1. Клик по кнопке с CSS-классом
# Создайте скрипт lesson05_task1.py.
# Открыть браузер Google Chrome.(Firefox)
# Перейти на страницу: http://uitestingplayground.com/classattr.
# Кликнуть на синюю кнопку.
# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Устанавливаем и запускаем драйвер
service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("http://uitestingplayground.com/classattr")
sleep(1)
blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
blue_button.click()
sleep(2)
driver.quit()
