from selenium.webdriver.common.by import By
from utilities.waits import wait_clickable

class CartPage:
    def __init__(self,driver):
        self.driver = driver

    add_to_cart=(By.ID,"add-to-cart")
    cart_icon=(By.XPATH,"//a[@class='shopping_cart_link']")
    checkout=(By.ID,"checkout")

    def add_product_to_cart(self):
        wait_clickable(self.driver,self.add_to_cart).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def click_checkout(self):
        self.driver.find_element(*self.checkout).click()