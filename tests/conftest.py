import os

import pytest
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "platformVersion": "12.0",
        "deviceName": "Samsung Galaxy S22 Ultra",

        "app": os.getenv('APP_URL'),
        "appWaitActivity": "org.wikipedia.*",

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": os.getenv('USER_NAME'),
            "accessKey": os.getenv('ACCESS_KEY')
        }
    })

    browser.config.driver_remote_url = str(os.getenv('remote_url', 'http://hub.browserstack.com/wd/hub'))
    browser.config.driver_options = options
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()


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

    yield

    browser.quit()