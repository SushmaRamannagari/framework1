from selenium.webdriver.common.by import By
from utilities.waits import wait_clickable
class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    product=(By.XPATH,"//div[text()='Sauce Labs Backpack']")
    title=(By.CLASS_NAME,"title")

    def select_product(self):
        wait_clickable(self.driver,self.product).click()
        