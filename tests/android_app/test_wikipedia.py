import pytest

from config import settings
from hw_20_mobile_automation.models.applications import app

if settings.platformName == 'ios':
    pytest.skip("Skipping tests for ios platform", allow_module_level=True)


def test_get_started_page(mobile_management):
    app.get_started_page.should_have_special_text(page=1, text='The Free Encyclopedia\n…in over 300 languages')
    app.get_started_page.click_on_continue()

    app.get_started_page.should_have_special_text(page=2, text='New ways to explore')
    app.get_started_page.click_on_continue()

    app.get_started_page.should_have_special_text(page=3, text='Reading lists with sync')
    app.get_started_page.click_on_continue()

    app.get_started_page.should_have_special_text(page=4, text='Data & Privacy')
    app.get_started_page.click_on_get_started()
    app.general_page.should_have_main_search()


def test_search(mobile_management):
    app.get_started_page.skip_get_started_page()

    app.general_page.click_to_main_search()
    app.general_page.enter_text_in_search_line('Appium')

    app.general_page.should_have_special_search_result()


def test_open_first_search_result_and_verify(mobile_management):
    app.get_started_page.skip_get_started_page()

    app.general_page.click_to_main_search()
    app.general_page.enter_text_in_search_line('Trouble')

    app.general_page.open_first_search_result()
    app.general_page.should_have_special_result_on_first_page()
