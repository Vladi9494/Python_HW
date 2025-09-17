# Шаг 2. Написание теста с использованием pytest
# Файл test_search.py содержит текст:
# Используется фикстура driver  для запуска и закрытия веб-драйвера.
# Проверяется функциональность поиска, используя метод search_for,
# и подтверждается наличие результатов.

import pytest
from selenium import webdriver
from gmain_page import GoogleMainPage

@pytest.fixture()
def driver():
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("https://www.google.com/")
  yield driver
  driver.quit()

def test_search(driver):
  page = GoogleMainPage(driver)
  page.search_for("Selenium Python")
  results = page.get_search_results()

  assert len(results) > 0, "Результаты поиска не найдены."