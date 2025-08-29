# II.  Переименовать кнопку
# Напишите скрипт.
# Шаги:
# 1. Перейдите на сайт http://uitestingplayground.com/textinput.
# 2. Укажите в поле ввода текст SkyPro.
# 3. Нажмите на синюю кнопку.
# 4. Получите текст кнопки и выведите в консоль ("SkyPro").

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

# $$("#newButtonName")
search_input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
search_input.send_keys("SkyPro")

# $$("#updatingButton")
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()

# $$("#updatingButton"))
flash = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
print(flash.text)
