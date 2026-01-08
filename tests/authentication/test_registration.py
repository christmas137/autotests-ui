import pytest
import allure
from tools.allure.tags import AllureTag
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@pytest.mark.registration
@pytest.mark.regression
class TestRegistration:
    @allure.title("Registration with correct email, username and password")
    def test_successful_registration(
        self,
        registration_page: RegistrationPage,
        dashboard_page: DashboardPage,
        random_user_for_registration: dict,
    ):
        registration_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
        )
        registration_page.registration_form.fill(
            email=random_user_for_registration["email"],
            username=random_user_for_registration["username"],
            password=random_user_for_registration["password"],
        )
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view.check_visible()
        
