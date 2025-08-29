# III. Дождаться картинки
# Напишите скрипт.
# Шаги:
# 1. Перейдите на сайт https://bonigarcia.dev
# /selenium-webdriver-java/loading-images.html.
# 2. Дождитесь загрузки всех картинок.
# 3. Получите значение атрибута src у 3-й картинки.
# 4. Выведите значение в консоль.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
           )

driver.maximize_window()

# информация об элементах которая может пригодиться:
# $$("#image-container")
# div = driver.find_element(By.CSS_SELECTOR, "#image-container")
# $$('img[src="img/award.png"]')

# Необходимое время (10 секунд) для загрузки всех 4-х картинок
# (или последней картинки "Пейзаж")
# $$("#landscape")
WebDriverWait(driver, 10).until(
         EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape")))

# Находим 3-ю картинку "Награда"
# $$("#award")
img = driver.find_element(By.CSS_SELECTOR, "#award")

# Получение значения атрибута "src" 3-ей картинки
f = img.get_attribute('src')

# Выводим значение атрибута "src", третьей картинки в консоль
print(img.get_attribute('src'))

driver.quit()
