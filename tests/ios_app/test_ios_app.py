import pytest

from config import settings
from hw_20_mobile_automation.models.applications import app

if settings.platformName == 'android':
    pytest.skip("Skipping tests for android platform", allow_module_level=True)


def test_ui_elements_for_one_input():
    app.ios_app_general_page.click_on_text_button()
    app.ios_app_general_page.enter_text('hello@browserstack.com')

    app.ios_app_general_page.should_have_special_text('hello@browserstack.com')


def test_ui_elements_for_two_inputs():
    app.ios_app_general_page.click_on_text_button()
    app.ios_app_general_page.enter_text('hello@browserstack.com')
    app.ios_app_general_page.enter_text('goodbuy@browserstack.com')

    app.ios_app_general_page.should_have_special_text('goodbuy@browserstack.com')
