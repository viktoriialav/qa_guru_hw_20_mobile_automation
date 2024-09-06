from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class GetStartedPage:
    def click_on_continue(self):
        with step('Open the next page'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    def click_on_get_started(self):
        with step('Open the main page'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()

    def skip_get_started_page(self):
        with step('Skip \'Get started\' page'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    def should_have_special_text(self, text, page=None):
        with step(f'Check the text {'on the ' * bool(page) + str(page) + ' page' * bool(page)}'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
                have.exact_text(text))
