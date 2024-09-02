import allure
import requests


def attach_screenshot(browser):
    allure.attach(body=browser.driver.get_screenshot_as_png(),
                  name='screenshot',
                  attachment_type=allure.attachment_type.PNG)


def attach_page_source(browser):
    allure.attach(body=browser.driver.page_source,
                  name='screen xml dump',
                  attachment_type=allure.attachment_type.XML)


def attach_video(session_id, user_name, access_key):
    browserstack_session = requests.get(url=f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
                                        auth=(user_name, access_key)).json()

    video_url = browserstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )
