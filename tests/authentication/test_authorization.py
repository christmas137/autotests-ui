import pytest
import allure
from tools.allure.tags import AllureTag
from pages.authentication.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage


@pytest.mark.authorization
@pytest.mark.regression
@allure.tag(AllureTag.AUTHORIZATION, AllureTag.REGRESSION)
class TestAuthorization:
    login = {
        "user.name1@gmail.com": "password",
        "user.name2@gmail.com": "  ",
        "  ": "password",
    }

    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with wrong email or password")
    @pytest.mark.parametrize("email, password", login.items())
    def test_wrong_email_or_password_authorization(
        self, login_page: LoginPage, email: str, password: str
    ):
        login_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
        )
        login_page.login_form.fill(email, password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with correct email and password")
    def test_successful_authorization(
        self,
        login_page: LoginPage,
        dashboard_page: DashboardPage,
        registration_page: RegistrationPage
    ):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(email="user.name@gmail.com", username="username", password="password")
        registration_page.registration_button.click()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email="user.name@gmail.com", password="password")
        login_page.click_login_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()
    
    @allure.tag(AllureTag.NAVIGATION)
    @allure.title("Navigation from login page to registration page")
    def test_navigate_from_authorization_to_registration(self, registration_page: RegistrationPage, login_page: LoginPage):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email="", username="", password="")   

