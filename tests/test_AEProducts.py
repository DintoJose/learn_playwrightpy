from pages.AE_Homepage import AEHomePage
from pages.AE_Productspage import AEProductsPage
from playwright.sync_api import Page, expect


def test_ae_products(page: Page, ae_page: AEHomePage, ae_products: AEProductsPage):
    ae_page.load()
    ae_page.clickprod()
    expect(page).to_have_title("Automation Exercise - All Products")
    ae_products.viewproduct(0)
    expect(page).to_have_title("Automation Exercise - Product Details")