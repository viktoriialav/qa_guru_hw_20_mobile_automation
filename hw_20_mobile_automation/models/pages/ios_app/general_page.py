from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class GeneralPage:
    def click_on_text_button(self):
        with step('Open text menu'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()

    def enter_text(self, value):
        with step('Enter the text:'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).type(value).press_enter()

    def should_have_special_text(self, value):
        with step('Verify found content'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output')).should(have.text(value))