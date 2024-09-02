from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have


class GeneralPage():
    def __init__(self):
        self.main_search = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia'))

    def should_have_main_search(self):
        with step('Check the main search line'):
            self.main_search.should(be.visible)

    def click_to_main_search(self):
        self.main_search.click()

    def enter_text_in_search_line(self, text):
        with step('Type serach'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(text)

    def should_have_special_search_result(self):
        with step('Verify found content'):
            results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
            results.should(have.size_greater_than(0))
            results.first.should(have.text('Appium'))

    def open_first_search_result(self):
        with step('Open the first search result'):
            browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.click()

    def should_have_special_result_on_first_page(self):
        with step('Verify found result'):
            browser.element((AppiumBy.CLASS_NAME, 'android.webkit.WebView')).all(
                (AppiumBy.CLASS_NAME, 'android.widget.TextView')).first.should(have.text('Trouble'))
