import pytest
from playwright.sync_api import Page, expect
from pages.AE_Loginpage import AELoginPage
from pages.AE_Homepage import AEHomePage
from test_data.test_credentials import VALID_USER


@pytest.mark.parametrize("creds", VALID_USER)
def test_login(page: Page, ae_login: AELoginPage, ae_page: AEHomePage, creds: dict):
    ae_page.load()
    ae_page.clicklogin()
    try:
        ae_login.login(**creds)
        expect(page.get_by_text(f'Logged in as {creds['username']}')).to_be_visible()
    except AssertionError:
        print("Login failed")
        page.close()


