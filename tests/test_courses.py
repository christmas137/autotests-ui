import pytest
from playwright.sync_api import Page, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_title_toolbar = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
        expect(courses_title_toolbar).to_contain_text("Courses")

        courses_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
        expect(courses_icon).to_be_visible()

        courses_title = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
        expect(courses_title).to_have_text("There is no results")

        courses_description = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
        expect(courses_description).to_have_text("Results from the load test pipeline will be displayed here")