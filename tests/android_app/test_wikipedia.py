import pytest
from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

samsung_s22_ultra = pytest.mark.parametrize('mobile_management',
                                            [('android', '12.0', 'Samsung Galaxy S22 Ultra')],
                                            indirect=True)
google_pixel_7_pro = pytest.mark.parametrize('mobile_management',
                                             [('android', '13.0', 'Google Pixel 7 Pro')],
                                             indirect=True)


@samsung_s22_ultra
def test_search(mobile_management):
    with step('Type search'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Appium')

    with step('Verify found content'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@google_pixel_7_pro
def test_open_search_result_and_verify(mobile_management):
    with step('Type search'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Trouble')

    with step('Verify found content'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.click()
        browser.element((AppiumBy.CLASS_NAME, 'android.webkit.WebView')).all(
            (AppiumBy.CLASS_NAME, 'android.widget.TextView')).first.should(have.text('Trouble'))
