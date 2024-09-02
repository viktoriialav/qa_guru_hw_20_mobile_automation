import pytest
from appium import webdriver
from selene import browser

import config
from hw_20_mobile_automation.utils import allure_browserstack


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    browser.config.driver = webdriver.Remote(command_executor=config.settings.remote_url,
                                             options=config.settings.driver_options)

    browser.config.timeout = config.settings.timeout

    yield

    session_id = browser.driver.session_id
    allure_browserstack.attach_screenshot(browser)
    allure_browserstack.attach_page_source(browser)

    browser.quit()

    if config.settings.access_key:
        allure_browserstack.attach_video(session_id, config.settings.user_name, config.settings.access_key)
