import pytest
import allure
from tools.allure.tags import AllureTag
from playwright.sync_api import Page
from fixtures.pages import CreateCoursePage, CoursesListPage
from pages.courses.courses_list_page import CoursesListPage


@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    @allure.title("Create course")
    def test_create_course(
        self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage
    ):
        create_course_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create"
        )
        create_course_page.create_course_toolbar_view.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="", estimated_time="", description="", max_score="0", min_score="0"
        )
        create_course_page.create_course_exercise_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image(
            "./testdata/files/image.png"
        )
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10",
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks",
        )
    
    @allure.title("Check displaying of empty courses list")
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
        )
        courses_list_page.navbar.check_visible("username")

        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title("Edit course")
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_form.fill(title="Anime", estimated_time="77", description='Anime page create', max_score="10", min_score="1")
        create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.course_view.check_visible(index=0, title="Anime", max_score="10", min_score="1", estimated_time="77")
        courses_list_page.course_view_menu.click_edit(index=0)

        create_course_page.create_course_form.fill(title="New title", estimated_time="22", description="New description", max_score="5", min_score="5")
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.course_view.check_visible(index=0, title="New title", estimated_time="22", max_score="5", min_score="5")



        
        