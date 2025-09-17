from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Создать класс для страницы авторизации, который будет содержать методы
# для ввода логина и пароля, а также для нажатия кнопки входа.
class Autorization:
    def __init__(self, driver):
        self.driver = driver  
        self.driver.get("https://www.saucedemo.com/")

    sleep(6)
    def input_login(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
    sleep(4)    
        
    