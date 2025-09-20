from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 6)

    def setting_waiting(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(
            By.CSS_SELECTOR, "#delay").send_keys("45")

    def calculator_buttons(self):
        self.driver.find_element(
            By.XPATH, "//*[@class='keys']/span[1]").click()
        self.driver.find_element(
            By.XPATH, "//*[@class='keys']/span[4]").click()
        self.driver.find_element(
            By.XPATH, "//*[@class='keys']/span[2]").click()
        self.driver.find_element(
            By.XPATH, "//*[@class='keys']/span[15]").click()
        # Ожидание перед извлечением результата
        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, "[class = 'screen']"), "15"))

    def result(self):
        res = self.driver.find_element(
            By.CSS_SELECTOR, "[class = 'screen']").text
        return res == "15"

    def close_driver(self):
        self.driver.quit()

