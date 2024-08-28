import pytest
from appium import webdriver
from selene import browser

import config
from hw_19_mobile_automation.utils import allure_browserstack


@pytest.fixture(scope='function', params=[('android', '12.0', 'Samsung Galaxy S22 Ultra'),
                                          ('android', '13.0', 'Google Pixel 7 Pro'),
                                          ('android', '11.0', 'OnePlus 9'),
                                          ('ios', '16', 'iPhone 14 Pro Max'),
                                          ('ios', '15', 'iPhone XS'),
                                          ('ios', '14', 'iPhone 11')])
def mobile_management(request):
    platform_name, platform_version, device_name = request.param
    initial_options = config.settings
    initial_options.platformName = platform_name
    initial_options.platformVersion = platform_version
    initial_options.deviceName = device_name
    options = initial_options.driver_options

    browser.config.driver = webdriver.Remote(command_executor=config.settings.remote_url,
                                             options=options)

    browser.config.timeout = config.settings.timeout

    yield

    session_id = browser.driver.session_id
    allure_browserstack.attach_screenshot(browser)
    allure_browserstack.attach_page_source(browser)

    browser.quit()

    allure_browserstack.attach_video(session_id, config.settings.user_name, config.settings.access_key)
