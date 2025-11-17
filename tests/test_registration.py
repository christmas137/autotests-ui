import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.registration
@pytest.mark.regression
def test_successful_registration(
    registration_page: RegistrationPage,
    dashboard_page: DashboardPage,
    random_user_for_registration: dict,
):
    registration_page.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    )
    registration_page.fill_registration_form(
        email=random_user_for_registration["email"],
        username=random_user_for_registration["username"],
        password=random_user_for_registration["password"],
    )
    registration_page.click_registration_button()
    dashboard_page.verify_title_on_dashboard()
