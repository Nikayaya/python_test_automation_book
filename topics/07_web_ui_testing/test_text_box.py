import pytest
from playwright.sync_api import sync_playwright
from text_box_page import TextBoxPage


def test_text_box_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        text_box_page = TextBoxPage(page)
        text_box_page.navigate()

        # Add data
        text_box_page.enter_full_name("Donald Duck")
        text_box_page.enter_email("donald.duck@example.com")
        text_box_page.enter_current_address("56 Main St")
        text_box_page.enter_permanent_address("379 Apple Rd")

        # Submit the form
        text_box_page.click_submit()

        # Check that the data is displayed as expected
        form_data = text_box_page.get_submitted_form_data()
        assert "Name:Donald Duck" in form_data['name']
        assert "Email:donald.duck@example.com" in form_data['email']
        assert "Current Address :56 Main St" in form_data['current_address']
        assert "Permananet Address :379 Apple Rd" in form_data['permanent_address']

        browser.close()
