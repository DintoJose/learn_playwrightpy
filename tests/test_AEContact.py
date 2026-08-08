import allure
from playwright.sync_api import Page, expect
import pytest

from pages.AE_Contactpage import AEContactPage
from pages.AE_Homepage import AEHomePage

@pytest.mark.headed_only
@allure.testcase("TC01", "Verify Contact Form Submission")
def test_contact_form(page: Page, ae_page: AEHomePage, ae_contact: AEContactPage):
    ae_page.load()
    ae_page.go_to_contact()
    ae_contact.fill_contact_form(
        name="Test User",
        email="test@test.com",
        subject="Test Subject",
        message="This is a test message"
    )
    ae_contact.upload_file("test_data/sample.txt")
    ae_contact.submit_form_and_accept_dialog()
    expect(ae_contact.success_message).to_be_visible()