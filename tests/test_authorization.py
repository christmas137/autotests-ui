import pytest
from pages.login_page import LoginPage

login = {
    "user.name1@gmail.com": "password",
    "user.name2@gmail.com": "  ",
    "  ": "password",
}


@pytest.mark.parametrize("email, password", login.items())
def test_wrong_email_or_password_authorization(
    login_page: LoginPage, email: str, password: str
):
    login_page.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
    )
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()
