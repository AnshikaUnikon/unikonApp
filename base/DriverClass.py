import flutter
from appium.options.android import UiAutomator2Options
from appium import webdriver


class Driver:
    def getDriverMethod(self):
        capabilities = dict(
            platformName='Android',
            # automationName='Flutter',
            # deviceName='Pixxel 3a API 34',
            deviceName='Galaxy S21 FE 5G',
            app='/Users/apple/Downloads/app-qa-release.apk',
            udid='RZCW91MRP6W'
        )
        appium_server_url = 'http://0.0.0.0:4723/wd/hub'
        options = UiAutomator2Options().load_capabilities(capabilities)
        driver = webdriver.Remote(command_executor=appium_server_url, options=options)

        return driver
