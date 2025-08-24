# Упражнение 3. Поле ввода
# Создайте скрипт lesson05_task3.py.
# Открыть браузер FireFox.
# Перейти на страницу: http://the-internet.herokuapp.com/inputs.
# Ввести в поле текст Sky.
# Очистить это поле (метод clear()).
# Ввести в поле текст Pro.
# Закрыть браузер (метод quit()).

# версия Firefox браузера 142.0   (64-разрядный)
# версия geckodriver v0.36.0-win64

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

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(2)
search_input = driver.find_element(By.CSS_SELECTOR, "[type='number']")
search_input.send_keys("Sky")
sleep(2)
search_input.clear()
sleep(2)
search_input.send_keys("Pro")
sleep(2)

driver.quit()
