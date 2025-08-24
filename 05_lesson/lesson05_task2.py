# Упражнение 2. Клик по кнопке без ID
# Создайте скрипт lesson05_task2.py.
# Открыть браузер Google Chrome.
# Перейти на страницу: http://uitestingplayground.com/dynamicid.
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

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/dynamicid")

# class = "btn btn-primary"

blue_button = driver.find_element(
    By.CSS_SELECTOR, "button[class='btn btn-primary']")
blue_button.click()

# ИЛИ ↓↓↓
# search_box = driver.find_element(By.XPATH,
# "//button[contains(text(), 'Button with Dynamic ID')]").click()

sleep(5)
driver.quit()
