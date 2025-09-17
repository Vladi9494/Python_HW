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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calclator(driver):
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.setting_waiting()
    calc_page.calculator_buttons()
    calc_page.result()
    # Ожидание перед извлечением результата
    result = calc_page.result()

    # Поиск элемента и извлечние текста
    result_element = driver.find_element(By.CSS_SELECTOR, "[class = 'screen']")
    result = result_element.text.strip()

    # Ожидание перед извлечением результата
    WebDriverWait(driver, 45).until(EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, "[class = 'screen']"), "15"))

    # Проверка результата
    result_element = driver.find_element(By.CSS_SELECTOR, "[class = 'screen']")
    result = result_element.text.strip()
    assert result == "15"

    calc_page.close_driver()
