from pages.AE_Homepage import AEHomePage
from playwright.sync_api import Page, expect

def test_home(page: Page, ae_page: AEHomePage):
    ae_page.load()
    expect(page).to_have_title("Automation Exercise")
