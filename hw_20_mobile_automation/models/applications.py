from hw_20_mobile_automation.models.pages.get_started_page import GetStartedPage
from hw_20_mobile_automation.models.pages.general_page import GeneralPage


class ApplicationManager:
    def __init__(self):
        self.general_page = GeneralPage()
        self.get_started_page = GetStartedPage()


app = ApplicationManager()