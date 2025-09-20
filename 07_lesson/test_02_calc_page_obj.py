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
    result = calc_page.get_result()
    assert result == "15"

    calc_page.close_driver()
