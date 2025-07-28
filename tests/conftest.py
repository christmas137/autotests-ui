import pytest
from playwright.sync_api import Playwright, Page, expect


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> Page:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        registration_button = page.get_by_test_id("registration-page-registration-button")
        expect(registration_button).to_be_disabled()

        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        expect(registration_email_input).to_be_visible()
        registration_email_input.fill("user.name@gmail.com")

        registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        expect(registration_username_input).to_be_visible()
        registration_username_input.fill("username")

        registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        expect(registration_password_input).to_be_visible()
        registration_password_input.fill("password")

        expect(registration_button).not_to_be_disabled()
        registration_button.click()

        context.storage_state(path="browser-state.json")
        browser.close()  

@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch()
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    yield page
    browser.close()
        