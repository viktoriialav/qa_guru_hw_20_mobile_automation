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
        # Specify device and os_version for testing
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": os.getenv('USER_NAME'),
            "accessKey": os.getenv('ACCESS_KEY')
        }
    })

    browser.config.driver_remote_url = str(os.getenv('remote_url', 'http://hub.browserstack.com/wd/hub'))
    browser.config.driver_options = options
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()
