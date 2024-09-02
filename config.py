import os
from typing import Optional, Literal

import dotenv
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from pydantic_settings import BaseSettings

from hw_20_mobile_automation.utils import path

EnvContext = Literal['local_emulator', 'local_real', 'bstack_android', 'bstack_ios']


class Settings(BaseSettings):
    context: EnvContext = 'local_emulator'

    # Appium Capabilities
    platformName: Optional[str] = 'wikipedia'
    udid: Optional[str] = 'emulator-5554'
    platformVersion: Optional[str] = None
    deviceName: Optional[str] = 'Pixel 8 API 33'
    app: Optional[str] = None
    appWaitActivity: Optional[str] = 'org.wikipedia.*'

    # BrowserStack Capabilities
    projectName: Optional[str] = None
    buildName: Optional[str] = None
    session_name: Optional[str] = None

    # BrowserStack credential
    user_name: Optional[str] = None
    access_key: Optional[str] = None

    # Remote driver
    remote_url: Optional[str] = None

    # Selene settings
    timeout: float = 10.0

    @property
    def driver_options(self):
        if self.platformName == 'android':
            options = UiAutomator2Options()
        else:
            options = XCUITestOptions()

        options.device_name = self.deviceName
        options.udid = self.udid
        options.platform_name = self.platformName
        options.platform_version = self.platformVersion
        options.app = self.app if (self.app.startswith('/') or self.app.startswith('bs://') or self.app.startswith(
            'C:\\')) else path.abs_path_from_root(self.app)
        options.app_wait_activity = self.appWaitActivity

        if 'hub.browserstack.com' in self.remote_url:
            dotenv.load_dotenv(path.abs_path_from_root('.env.bstack_credential'))
            options.load_capabilities(
                {
                    'bstack:options': {
                        "projectName": self.projectName,
                        "buildName": self.buildName,
                        "sessionName": self.session_name,

                        "userName": os.getenv('bstack_userName'),
                        "accessKey": os.getenv('bstack_accessKey')
                    }
                }
            )
        return options

    @classmethod
    def in_context(cls, env: Optional[EnvContext] = None) -> 'Settings':
        env = env or cls().context
        return cls(_env_file=path.abs_path_from_root(f'.env.{env}'))


settings = Settings.in_context()
