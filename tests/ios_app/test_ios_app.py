import pytest
from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from config import settings


if settings.platformName == 'android':
    pytest.skip("Skipping tests for ios platform", allow_module_level=True)


def test_ui_elements_for_one_input():
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).type('hello@browserstack.com').press_enter()

    with step('Verify found content'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output')).should(have.text('hello@browserstack.com'))


def test_ui_elements_for_two_inputs():
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).type('hello@browserstack.com').press_enter()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).type('goodbuy@browserstack.com').press_enter()

    with step('Verify found content'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output')).should(have.text('goodbuy@browserstack.com'))
