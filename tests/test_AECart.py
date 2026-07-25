from playwright.sync_api import Page, expect, Route
import pytest

from pages.AE_Homepage import AEHomePage
from pages.AE_Productspage import AEProductsPage
from pages.AE_Cartpage import AECartPage
from pages.AE_Loginpage import AELoginPage
from pages.AE_Checkoutpage import AECheckoutPage

def test_cart_remove(page: Page, ae_cart: AECartPage,
ae_page: AEHomePage):
    ae_page.load()
    ae_page.addtocart_home(0)
    ae_page.go_to_cart_home()
    expect(page).to_have_title("Automation Exercise - Checkout")
    expect(ae_cart.checkout_button).to_be_visible()
    # expect(ae_cart.order_details).to_be_visible()
    ae_cart.remove_item(0)
    expect(ae_cart.back_to_products).to_be_visible()

def test_checkout_without_login(page: Page, ae_cart: AECartPage,
ae_page: AEHomePage):
    ae_page.load()
    ae_page.addtocart_home(0)
    ae_page.go_to_cart_home()
    expect(ae_cart.checkout_button).to_be_visible()
    ae_cart.checkout()
    expect(ae_cart.register_link).to_be_visible()

def test_checkout_after_login(page: Page, ae_login: AELoginPage, ae_page: AEHomePage, ae_cart: AECartPage, ae_checkout: AECheckoutPage):
    ae_page.load()
    ae_page.clicklogin()
    ae_login.login("1test12345@email.com","1test12345","1test12345")
    ae_page.addtocart_home(0)
    ae_page.go_to_cart_home()
    expect(ae_cart.checkout_button).to_be_visible()
    ae_cart.checkout()
    expect(ae_checkout.order_button).to_be_visible()
    ae_checkout.place_order()
    expect(page).to_have_title("Automation Exercise - Payment")


