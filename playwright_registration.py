from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright: 
   chromium = playwright.chromium.launch(headless=False)
   page = chromium.new_page()
   page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

   registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
   expect(registration_email_input).to_be_visible()
   registration_email_input.fill("user.name@gmail.com")

   registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
   expect(registration_username_input).to_be_visible()
   registration_username_input.fill("username")

   registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
   expect(registration_password_input).to_be_visible()
   registration_password_input.fill("password")

   registration_button = page.get_by_test_id("registration-page-registration-button")
   expect(registration_button).to_be_visible()
   registration_button.click()

   h6_dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")
   expect(h6_dashboard_title).to_contain_text("Dashboard")



