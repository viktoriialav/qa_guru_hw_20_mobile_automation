import pytest
from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

iphone_14_pro_max = pytest.mark.parametrize('mobile_management',
                                            [('ios', '16', 'iPhone 14 Pro Max')],
                                            indirect=True)
iphone_xs = pytest.mark.parametrize('mobile_management',
                                    [('ios', '15', 'iPhone XS')],
                                    indirect=True)


@iphone_14_pro_max
def test_ui_elements_for_one_input(mobile_management):
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).type('hello@browserstack.com').press_enter()

    with step('Verify found content'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output')).should(have.text('hello@browserstack.com'))


@iphone_xs
def test_ui_elements_for_two_inputs(mobile_management):
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).type('hello@browserstack.com').press_enter()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).type('goodbuy@browserstack.com').press_enter()

    with step('Verify found content'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output')).should(have.text('goodbuy@browserstack.com'))
