from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self,driver):
        self.driver = driver

    first_name=(By.ID,"first-name")
    last_name=(By.ID,"last-name")
    postal_code=(By.ID,"postal-code")
    continue_btn = (By.ID, "continue")
    finish_btn=(By.ID, "finish")
    confirmation = (By.ID,"checkout_complete_container")

    def enter_details(self, fname, lname, zip_code):
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(zip_code)
        self.driver.find_element(*self.continue_btn).click()

    def finish_order(self):
        self.driver.find_element(*self.finish_btn).click()

    def get_confirmation(self):
        self.driver.find_element(*self.confirmation).click()