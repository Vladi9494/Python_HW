# I Форма
# Шаги:
# 1. Откройте страницу: https://bonigarcia.dev
# /selenium-webdriver-java/data-types.html в Edge или Safari.
# 2. Заполните форму значениями:
# First name    Иван
# Last name     Петров
# Address       Ленина, 55-3
# Email         test@skypro.com
# Phone number  +7985899998787
# Zip code      *оставить пустым
# City          Москва
# Country       Россия
# Job position  QA
# Company       SkyPro

# 3. Нажмите кнопку Submit.
# 4. Проверьте (assert), что поле Zip code подсвечено красным.
# 5. Проверьте (assert), что остальные поля подсвечены зеленым.

# import pytest
# from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# driver = webdriver.Edge(service=EdgeService(
#    EdgeChromiumDriverManager().install()))


def test_data_types():
    edge_driver_path = (r"C:\Users\0\Desktop\ПИТОН_ДОМАШКИ\ДОМАШКИ_по_PYTHON"
                        r"\Python_HW\05_lesson\msedgedriver.exe")

    driver = webdriver.Edge(service=EdgeService(edge_driver_path))

    driver.maximize_window()

    driver.get("https://bonigarcia.dev"
               "/selenium-webdriver-java/data-types.html")
    print("Сайт открыт")

    search_input = driver.find_element(By.NAME, "first-name")
    search_input.send_keys("Иван")

    search_input = driver.find_element(By.NAME, "last-name")
    search_input.send_keys("Петров")

    search_input = driver.find_element(By.NAME, "address")
    search_input.send_keys("Ленина, 55-3")

    search_input = driver.find_element(By.NAME, "city")
    search_input.send_keys("Москва")

    search_input = driver.find_element(By.NAME, "country")
    search_input.send_keys("Россия")

    search_input = driver.find_element(By.NAME, "e-mail")
    search_input.send_keys("test@skypro.com")

    search_input = driver.find_element(By.NAME, "phone")
    search_input.send_keys("+7985899998787")

    search_input = driver.find_element(By.NAME, "job-position")
    search_input.send_keys("QA")

    search_input = driver.find_element(By.NAME, "company")
    search_input.send_keys("SkyPro")
    # company = WebDriverWait(driver, 20).until(
    # EC.visibility_of_element_located(
    # (By.NAME, "company"))).send_keys("SkyPro")

    print("Поля заполнены")
    # $x(By.XPATH, "//button[@type='submit']")
    # $$(By.CSS_SELECTOR, "button[class='btn btn-outline-primary mt-3']")
    # Проверка кликабельности кнопки "Submit"
    # button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    # $x(By.XPATH, "//button[@type='submit']")))
    # $$("html.h-100")
    # Прокрутка вниз
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("прокрутка вниз выполнена")
    button = driver.find_element(By.XPATH, "//button[@type='submit']")
    driver.execute_script("arguments[0].click();", button)
    print('Кнопка "Submit" найдена')
    print("Кнопка 'Submit' нажата")
    print("Страница с подсветкой полей открыта")
    # wait = WebDriverWait(driver,10)
    # element = wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//button[@type='submit']")))
    # element.click()
    # button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    #      (By.XPATH, f"//button[@type='submit']"))).click()
    try:
        button = WebDriverWait(driver, 20).until(
           EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
            ).click()
    except TimeoutException:
        print("Кнопка не кликабельна в течение указанного времени ожидания")

    zip_code_field = driver.find_element(By.ID, "zip-code")
    border_color = driver.execute_script("return window.getComputedStyle("
                                         "arguments[0]).borderColor;",
                                         zip_code_field)
    assert border_color == "rgb(245, 194, 199)"
    # zip_fild = driver.find_element(By.ID, "zip-code")
    # zip_color = zip_fild.value_of_css_property("border-color")
    # assert zip_color == "rgb(245, 194, 199)"
    zip_fields = ["first-name", "last-name", "address", "e-mail", "phone",
                  "city", "country", "job-position", "company"]
    for zip_field in zip_fields:
        zip_fields = driver.find_element(
            By.CSS_SELECTOR, ".alert-success"
            ).value_of_css_property("border-color")
    assert zip_fields == "rgb(186, 219, 204)"
    driver.quit()

    # zip_fields = ["first-name", "last-name", "address", "e-mail", "phone",
    #               "city", "country", "job-position", "company"]
    # for zip_field in zip_fields:
    #     element_color = driver.find_element(
    #         By.ID, zip_field
    #         ).value_of_css_property("border-color")
    #     assert zip_field == "rgb(186, 219, 204)"
    #     f'Пришел цвет {element_color} у элементов {zip_fields}'
    # driver.quit()
