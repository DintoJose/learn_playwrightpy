from playwright.sync_api import Page

class AECheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.order_button = self.page.get_by_role("link", name="Place Order")

    def place_order(self):
        self.order_button.click()

    def handle_ad_popup(self):
        self.page.on("popup", lambda popup: popup.close())