from playwright.sync_api import Page

class AELoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.login_email = page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")
        self.login_password = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def login(self, email: str, password: str):
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click()

