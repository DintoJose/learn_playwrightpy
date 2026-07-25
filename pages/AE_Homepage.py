from playwright.sync_api import Page

class AEHomePage:

    def __init__(self, page: Page):
        self.page = page
        self.product_page = page.get_by_role("link", name=" Products")
        self.login_page = page.get_by_role("link", name=" Signup / Login")
        self.add_to_cart_button = self.page.get_by_text("Add to cart")
        self.view_cart_button = self.page.get_by_role("link", name="View Cart")
        self.contact_button = self.page.get_by_role("link", name=" Contact us")

    def load(self):
        self.page.goto("https://automationexercise.com")

    def clickprod(self):
        self.product_page.click()

    def clicklogin(self):
        self.login_page.click()

    def addtocart_home(self, number: int):
        self.add_to_cart_button.nth(number).click()

    def go_to_cart_home(self):
        self.view_cart_button.click()

    def go_to_contact(self):
        self.contact_button.click()

