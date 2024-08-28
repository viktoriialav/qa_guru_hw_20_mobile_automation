from typing import Optional

import dotenv
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Appium Capabilities
    platformName: str = 'android'
    platformVersion: str = '12.0'
    deviceName: str = 'Samsung Galaxy S22 Ultra'
    app: Optional[str] = None

    # BrowserStack Capabilities
    projectName: Optional[str] = None
    buildName: Optional[str] = None
    session_name: Optional[str] = None

    # BrowserStack credential
    user_name: Optional[str] = None
    access_key: Optional[str] = None

    # Remote driver
    remote_url: str = 'http://hub.browserstack.com/wd/hub'

    # Selene settings
    timeout: float = 10.0

    @property
    def driver_options(self):
        if self.platformName == 'android':
            options = UiAutomator2Options()
        else:
            options = XCUITestOptions()
            self.app = 'bs://sample.app'

        options.device_name = self.deviceName
        options.platform_name = self.platformName
        options.platform_version = self.platformVersion
        options.app = self.app
        options.load_capabilities(
            {
                'bstack:options': {
                    "projectName": self.projectName,
                    "buildName": self.buildName,
                    "sessionName": self.session_name,

                    "userName": self.user_name,
                    "accessKey": self.access_key
                }
            }
        )
        return options


settings = Settings(_env_file=dotenv.find_dotenv('.env'))