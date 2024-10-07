import time
import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Setup Logging
logging.basicConfig(level=logging.INFO)

# Desired Capabilities for Appium
capabilities = {
    "platformName": "Android",
    "deviceName": "Galaxy S21 FE 5G",
    "app": "/Users/apple/Downloads/app-qa-release (11).apk",  # Replace with your app package
    "udid": "RZCW91MRP6W"
}

# Initialize the Appium Driver
appium_server_url = 'http://0.0.0.0:4723/wd/hub'
options = UiAutomator2Options().load_capabilities(capabilities)
driver = webdriver.Remote(command_executor=appium_server_url, options=options)

driver.implicitly_wait(10)
driver.find_element(by=AppiumBy.ID,value="com.android.permissioncontroller:id/permission_allow_button").click()
driver.find_element(by=AppiumBy.XPATH,value='//android.widget.Button[@content-desc="Get started"]').click()
driver.find_element(by=AppiumBy.XPATH,value='//android.widget.Button[@content-desc="Skip >"]').click()
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value='new UiSelector().resourceId("profile_tabbar_button")').click()
driver.find_element(by=AppiumBy.XPATH,value='//android.widget.EditText[@resource-id="phone_number_textfield"]').click()
driver.find_element(by=AppiumBy.XPATH,value='//android.widget.EditText[@resource-id="phone_number_textfield"]').send_keys('9555569476')
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value='new UiSelector().resourceId("continue_button")').click()
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value='new UiSelector().className("android.view.View").instance(17)').click()
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value='new UiSelector().className("android.view.View").instance(17)').send_keys("1111")