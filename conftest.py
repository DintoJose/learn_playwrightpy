import pytest
from playwright.sync_api import Page

from pages.AE_Checkoutpage import AECheckoutPage
from pages.AE_Homepage import AEHomePage
from pages.AE_Productspage import AEProductsPage
from pages.AE_Loginpage import AELoginPage
from pages.AE_Cartpage import AECartPage

@pytest.fixture
def ae_page(page: Page):
    return AEHomePage(page)

@pytest.fixture
def ae_products(page: Page):
    return AEProductsPage(page)

@pytest.fixture
def ae_login(page: Page):
    return AELoginPage(page)

@pytest.fixture
def ae_cart(page: Page):
    return AECartPage(page)

@pytest.fixture
def ae_checkout(page: Page):
    return AECheckoutPage(page)
