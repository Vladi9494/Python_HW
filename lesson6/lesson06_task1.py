# I. Нажать на кнопку
# Напишите скрипт.
# Шаги:
# 1. Перейдите на страницу http://uitestingplayground.com/ajax.
# 2. Нажмите на синюю кнопку.
# 3. Получите текст из зеленой плашки.
# 4. Выведите его в консоль
# # ("Data loaded with AJAX get request.").

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.implicitly_wait(16)
# Чтобы текст с зелёной плашли загрузился
# по сценарию неявного ожидания (15 секунд) не хватает, а (16 секунд) хватает.

driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# $$("p.bg-success")
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text  # ИЛИ ↓↓↓
# $$('p[class="bg-success"]')
# txt = content.find_element(By.CSS_SELECTOR, 'p[class="bg-success"]').text

print(txt)
