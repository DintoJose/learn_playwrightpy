from playwright.sync_api import Page

class AECartPage:
    def __init__(self, page: Page):
        self.page = page
        self.back_to_products = self.page.get_by_role("link", name="here")
        self.checkout_button = self.page.get_by_text("Proceed To Checkout")
        self.order_details = self.page.get_by_role("row")
        self.remove_from_cart_button = self.page.locator(".cart_quantity_delete")
        self.register_link = self.page.get_by_role("link", name="Register / Login")

    def checkout(self):
        self.checkout_button.click()

    def remove_item(self, item: int):
        self.remove_from_cart_button.nth(item).click()

    def register_for_checkout(self):
        self.register_link.click()

