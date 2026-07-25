import pytest
from playwright.sync_api import Page

from pages.AE_Checkoutpage import AECheckoutPage
from pages.AE_Homepage import AEHomePage
from pages.AE_Productspage import AEProductsPage
from pages.AE_Loginpage import AELoginPage
from pages.AE_Cartpage import AECartPage
from pages.AE_Contactpage import AEContactPage

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

@pytest.fixture
def ae_contact(page: Page):
    return AEContactPage(page)

def pytest_configure(config):
    config.addinivalue_line(
    "markers", "headed_only: Skipped in headless mode - Cloudflare protection"
    )

@pytest.fixture(autouse=True)
def skip_if_headless(request):
    if request.node.get_closest_marker("headed_only")and not request.config.getoption("--headed", default = False):
        pytest.skip("Skipping test in headless mode - Cloudflare protection")

@pytest.fixture
def page(page: Page):
    def handle_route(route):
        if any(domain in route.request.url for domain in [
            "googleads", 
            "doubleclick.net", 
            "adsbygoogle"
            ]):
            route.abort()
        else:
            route.continue_()
    page.route("**/*", handle_route)
    return page