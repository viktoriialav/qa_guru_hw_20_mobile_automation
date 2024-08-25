import os

import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver
from dotenv import load_dotenv
from selene import browser

from hw_19_mobile_automation.utils import allure_web, allure_browserstack


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', params=[('android', '12.0', 'Samsung Galaxy S22 Ultra'),
                                          ('android', '13.0', 'Google Pixel 7 Pro'),
                                          ('android', '11.0', 'OnePlus 9'),
                                          ('ios', '16', 'iPhone 14 Pro Max'),
                                          ('ios', '15', 'iPhone XS'),
                                          ('ios', '14', 'iPhone 11')])
def mobile_management(request):
    platform_name, platform_version, device_name = request.param
    user_name = os.getenv('USER_NAME')
    access_key = os.getenv('ACCESS_KEY')
    capabilities = {
        "platformName": platform_name,
        "platformVersion": platform_version,
        "deviceName": device_name,

        "app": 'bs://sample.app',

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": user_name,
            "accessKey": access_key
        }
    }

    if platform_name == 'android':
        capabilities['app'] = os.getenv('APP_URL')
        options = UiAutomator2Options().load_capabilities(capabilities)
    else:
        options = XCUITestOptions().load_capabilities(capabilities)

    browser.config.driver = webdriver.Remote(command_executor='http://hub.browserstack.com/wd/hub', options=options)
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    session_id = browser.driver.session_id
    allure_browserstack.attach_screenshot(browser)
    allure_browserstack.attach_page_source(browser)

    browser.quit()

    allure_browserstack.attach_video(session_id, user_name, access_key)
