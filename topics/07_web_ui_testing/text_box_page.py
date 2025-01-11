from playwright.sync_api import Page

class TextBoxPage:
    def __init__(self, page: Page):
        self.page = page
        self.full_name_input = page.locator('input#userName')
        self.email_input = page.locator('input#userEmail')
        self.current_address_input = page.locator('textarea#currentAddress')
        self.permanent_address_input = page.locator('textarea#permanentAddress')
        self.submit_button = page.locator('#submit')
        self.output_name = page.locator('#name')
        self.output_email = page.locator('#email')
        self.output_current_address = page.locator('p#currentAddress')
        self.output_permanent_address = page.locator('p#permanentAddress')

    def navigate(self):
        self.page.goto("https://demoqa.com/text-box")

    def enter_full_name(self, full_name: str):
        self.full_name_input.fill(full_name)

    def enter_email(self, email: str):
        self.email_input.fill(email)

    def enter_current_address(self, current_address: str):
        self.current_address_input.fill(current_address)

    def enter_permanent_address(self, permanent_address: str):
        self.permanent_address_input.fill(permanent_address)

    def click_submit(self):
        self.submit_button.click()

    def get_submitted_form_data(self):
        return {
            'name': self.output_name.text_content(),
            'email': self.output_email.text_content(),
            'current_address': self.output_current_address.text_content(),
            'permanent_address': self.output_permanent_address.text_content()
        }