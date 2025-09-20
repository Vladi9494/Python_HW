# Каждый тест может только создавать, настраивать и закрывать драйвер.
# Остальные selenium-методы (click, send_keys, text…)
# запрещены в коде тестов (должны быть в классах страниц).
# В классах страниц не должно быть проверок.

# Создание теста:
# Написать тест, который использует PageObject
# для выполнения следующих действий:
# Открыть страницу калькулятора.
# Ввести значение 45 в поле задержки (локатор #delay).
# Нажать кнопки: 7, +, 8, =.
# Проверить (assert), что в окне отобразится
# результат 15 через 45 секунд.

from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get(
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
    yield driver
    driver.quit()


def test_calclator(driver):
    calc_page = CalcPage(driver)
    calc_page.setting_waiting()
    calc_page.calculator_buttons()
    calc_page.result()
    # Ожидание перед извлечением результата
    result = calc_page.result()

    # Поиск элемента и извлечние текста
    result_element = driver.find_element(By.CSS_SELECTOR, "[class = 'screen']")
    result = result_element.text.strip()

    # Проверка результата
    result_element = driver.find_element(By.CSS_SELECTOR, "[class = 'screen']")
    result = result_element.text.strip()
    assert result == "15"

    calc_page.close_driver()
