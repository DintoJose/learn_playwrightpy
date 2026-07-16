from playwright.sync_api import Page, expect
from pages.AE_Loginpage import AELoginPage
from pages.AE_Homepage import AEHomePage
from test_data.test_credentials import VALID_USER

def test_login(page: Page, ae_login: AELoginPage, ae_page: AEHomePage):
    ae_page.load()
    ae_page.clicklogin()
    ae_login.login(**VALID_USER)
    expect(page.get_by_text("Logged in as 1test12345")).to_be_visible()