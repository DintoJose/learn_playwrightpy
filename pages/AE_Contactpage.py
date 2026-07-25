from playwright.sync_api import Page

class AEContactPage:

    def __init__(self, page: Page):
        self.page = page
        self.contact_name = page.get_by_role("textbox", name="Name")
        self.contact_email = page.get_by_role("textbox", name="Email", exact=True)
        self.contact_subject = page.get_by_role("textbox", name="Subject")
        self.contact_message = page.get_by_role("textbox", name="Your Message Here")
        self.file_upload = page.get_by_role("button", name="Choose File")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.success_message = page.locator("#contact-page").get_by_text("Success! Your details have")

    def enter_name(self, name: str):
        self.contact_name.fill(name)

    def enter_email(self, email: str):
        self.contact_email.fill(email)

    def enter_subject(self, subject: str):
        self.contact_subject.fill(subject)

    def enter_message(self, message: str):
        self.contact_message.fill(message)

    def upload_file(self, file_path: str):
        self.file_upload.set_input_files(file_path)

    def submit_form_and_accept_dialog(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.submit_button.click()
        self.page.wait_for_load_state("networkidle")
    
    def submit_form_and_reject_dialog(self):
        self.page.on("dialog", lambda dialog: dialog.dismiss())
        self.submit_button.click()
        self.page.wait_for_load_state("networkidle")

    def fill_contact_form(self, name: str, email: str, subject: str, message: str):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_subject(subject)
        self.enter_message(message)