# Упражнение 1. Клик по кнопке с CSS-классом
# Создайте скрипт lesson05_task1.py.
# Открыть браузер Google Chrome.
# Перейти на страницу: http://uitestingplayground.com/classattr.
# Кликнуть на синюю кнопку.
# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# options = webdriver.ChromeOptions()
# options.binary_location == r"C:\Users\0\AppData\Roaming
# \chrome-win64\chrome.exe", options == options

# btn class1 btn-primary btn-test

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://uitestingplayground.com/classattr")

sleep(1)
blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
blue_button.click()

sleep(3)
driver.quit()
