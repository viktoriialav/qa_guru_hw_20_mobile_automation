import os

import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver as app_webdriver
from dotenv import load_dotenv
from selene import browser
import selenium
from selenium.webdriver.chrome.options import Options

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

    browser.config.driver = app_webdriver.Remote(command_executor='http://hub.browserstack.com/wd/hub', options=options)
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    session_id = browser.driver.session_id
    allure_browserstack.attach_screenshot(browser)
    allure_browserstack.attach_page_source(browser)

    browser.quit()

    allure_browserstack.attach_video(session_id, user_name, access_key)


@pytest.fixture(scope='function')
def browser_management():
    browser.config.base_url = os.getenv(
        'base_url', 'https://www.wikipedia.org'
    )
    browser.config.driver_name = os.getenv('driver_name', 'chrome')
    browser.config.hold_driver_at_exit = (
        os.getenv('hold_driver_at_exit', 'false').lower() == 'true'
    )
    browser.config.window_width = os.getenv('window_width', '1024')
    browser.config.window_height = os.getenv('window_height', '768')
    browser.config.timeout = float(os.getenv('timeout', '3.0'))

    driver_options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": '125.0',
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    driver_options.capabilities.update(selenoid_capabilities)

    user_login = os.getenv('SELENOID_LOGIN')
    user_password = os.getenv('SELENOID_PASSWORD')
    selenoid_url = os.getenv('SELENOID_URL')
    driver = selenium.webdriver.Remote(
        command_executor=f'https://{user_login}:{user_password}@{selenoid_url}/wd/hub',
        options=driver_options)

    browser.config.driver = driver

    yield browser

    allure_web.attach_screenshot(browser)
    allure_web.attach_html(browser)
    allure_web.attach_logs(browser)
    allure_web.attach_video(browser)

    browser.quit()
