import allure

from pages.AE_Homepage import AEHomePage
from pages.AE_Productspage import AEProductsPage
from playwright.sync_api import Page, expect


@allure.testcase("TC01", "Verify View product details functionality")
def test_ae_products(page: Page, ae_page: AEHomePage, ae_products: AEProductsPage):
    ae_page.load()
    ae_page.clickprod()
    expect(page).to_have_title("Automation Exercise - All Products")
    ae_products.viewproduct(0)
    expect(page).to_have_title("Automation Exercise - Product Details")

@allure.testcase("TC02", "Verify Search Products functionality")
def test_search_products(page: Page, ae_page: AEHomePage, ae_products: AEProductsPage):
    ae_page.load()
    ae_page.clickprod()
    ae_products.search_product("Tshirt")
    expect(page.get_by_role("heading", name="Searched Products")).to_be_visible()