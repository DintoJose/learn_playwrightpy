from playwright.sync_api import Page, expect
from pages.AE_Homepage import AEHomePage
from pages.AE_Productspage import AEProductsPage
from pages.AE_Cartpage import AECartPage

def test_cart(page: Page, ae_cart: AECartPage,
ae_page: AEHomePage,
ae_products: AEProductsPage):
    ae_page.load()
    ae_page.addtocart_home(0)
    ae_page.go_to_cart_home()
    expect(page).to_have_title("Automation Exercise - Checkout")
    expect(ae_cart.checkout_button).to_be_visible()
    # expect(ae_cart.order_details).to_be_visible()
    ae_cart.remove_item(0)
    expect(ae_cart.back_to_products).to_be_visible()
