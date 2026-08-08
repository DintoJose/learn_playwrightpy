import allure

from pages.AE_Homepage import AEHomePage
from playwright.sync_api import Page, expect

@allure.testcase("TC01", "Verify Home Page Elements")
def test_home(page: Page, ae_page: AEHomePage):
    ae_page.load()
    expect(page).to_have_title("Automation Exercise")
    expect(page.get_by_role("link", name=" Home")).to_be_visible()
    expect(page.get_by_role("link", name=" Products")).to_be_visible()
    expect(page.get_by_role("link", name=" Cart")).to_be_visible()
    expect(page.get_by_role("link", name=" Signup / Login")).to_be_visible()
    expect(page.get_by_role("heading", name="Category")).to_be_visible()
    expect(page.get_by_role("heading", name="Features Items")).to_be_visible()
    expect(page.get_by_role("heading", name="Brands")).to_be_visible()


