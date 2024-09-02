from hw_20_mobile_automation.models.pages import wikipedia, ios_app


class ApplicationManager:
    def __init__(self):
        self.wikipedia_general_page = wikipedia.general_page.GeneralPage()
        self.wikipedia_get_started_page = wikipedia.get_started_page.GetStartedPage()
        self.ios_app_general_page = ios_app.general_page.GeneralPage()


app = ApplicationManager()
