# Упражнение 4. Форма авторизации
# Создайте скрипт lesson05_task4.py.
# Открыть браузер FireFox.
# Перейти на страницу http://the-internet.herokuapp.com/login.
# В поле username ввести значение tomsmith.
# В поле password ввести значение SuperSecretPassword!.
# Нажать кнопку Login.
# Вывести текст с зеленой плашки в консоль.
# Закрыть браузер (метод quit()).

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options

# Устанавливаем и запускаем драйвер
service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("http://the-internet.herokuapp.com/login")
sleep(2)
search_input = driver.find_element(By.NAME, "username")
search_input.send_keys("tomsmith")
sleep(2)
search_input = driver.find_element(By.NAME, "password")
search_input.send_keys("SuperSecretPassword!")
sleep(4)
button = driver.find_element(By.CSS_SELECTOR, "button[class='radius']")
button.click()
sleep(5)
flash = driver.find_element(By.CSS_SELECTOR, "div#flash-messages")
print(flash.text)
driver.quit()
