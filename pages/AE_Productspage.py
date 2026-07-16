from playwright.sync_api import Page

class AEProductsPage:

    def __init__(self, page: Page):
        self.page = page
        self.view_product_button = self.page.get_by_role("link", name=" View Product")
        self.add_to_cart_button = self.page.get_by_text("Add to cart")
        self.view_cart_button = self.page.get_by_role("link", name="View Cart")

    def viewproduct(self, number):
        self.view_product_button.nth(4).wait_for()
        self.view_product_button.nth(number).click()

    def addtocart(self, number: int):
        self.add_to_cart_button.nth(number).click()
