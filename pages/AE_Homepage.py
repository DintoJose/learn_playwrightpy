from playwright.sync_api import Page

class AEHomePage:

    def __init__(self, page: Page):
        self.page = page
        self.product_page = page.get_by_role("link", name=" Products")
        self.login_page = page.get_by_role("link", name=" Signup / Login")

    def load(self):
        self.page.goto("https://automationexercise.com")

    def clickprod(self):
        self.product_page.click()

    def clicklogin(self):
        self.login_page.click()

