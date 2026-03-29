import pytest

from configfiles.config import URL
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from testdata.data import *

def test_purchase(driver):
    driver.get(URL)

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    product=ProductPage(driver)
    product.select_product()

    cart=CartPage(driver)
    cart.add_product_to_cart()
    cart.go_to_cart()
    cart.click_checkout()

    checkout=CheckoutPage(driver)
    checkout.enter_details(FIRST_NAME, LAST_NAME, ZIP)
    checkout.finish_order()
    assert "Thank you for your order!" in checkout.get_confirmation()