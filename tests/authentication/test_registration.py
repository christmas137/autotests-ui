import pytest
import allure
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeture
from tools.allure.stories import AllureStory
from allure_commons.types import Severity
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeture.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeture.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
@pytest.mark.registration
@pytest.mark.regression
class TestRegistration:
    @allure.title("Registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)
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
        
