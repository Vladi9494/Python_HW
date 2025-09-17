from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создать класс для страницы корзины, который будет содержать методы
# для нажатия кнопки Checkout и проверки содержимого корзины.
class CartPage: 
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/cart.html")

    # нажатие кнопки "Checkout"
    def click_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "[id='checkout']").click()
    # проверка содержимого корзины
    def cart_contents(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        # assert cart_badge.text == "3", "В корзине должно быть 3 товара"
        


    # def cart_contents(self):
    #     return
    #     self.driver.find_element(By.CSS_SELECTOR, "#cart-content").text
        items = self.driver.find_elements(By.CSS_SELECTOR, "div.cart_item_label")
        content = "\n".join([item.text for item in items])
        return content
    
        self.driver.quit()