import time

import logging
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _notification_pop_up = 'com.android.permissioncontroller:id/permission_allow_button'
    _get_started_btn = '//android.widget.Button[@content-desc="Get started"]'
    _skip_btn = '//android.widget.Button[@content-desc="Skip >"]'
    _mobile_no = 'new UiSelector().resourceId("phone_number_textfield")'
    _continue_btn = 'new UiSelector().resourceId("continue_button")'
    _otp = 'new UiSelector().className("android.view.View").instance(17)'
    _verify_btn = '//android.widget.Button[@content-desc="Verify"]'
    _gmail_icon = 'new UiSelector().resourceId("google_login_button")'
    _gmail_select = '(//android.widget.LinearLayout[@resource-id="com.google.android.gms:id/container"])[2]/android.widget.LinearLayout'

    def launch_app(self):
        self.clickElement(self._notification_pop_up, "id")
        print("Click on Allow button")

        self.clickElement(self._get_started_btn, "xpath")
        print("Click on Get Started button")

        self.clickElement(self._skip_btn, "xpath")
        print("Click on Skip")

    def login_mobile_no(self):
        try:

            self.clickElement(self._mobile_no, "ui")
            self.sendText("9897123456", self._mobile_no, "ui")
            print("Mobile Number entered")

            self.driver.back()
            self.clickElement(self._continue_btn, "ui")
            print("Click on Continue button")

            self.clickElement(self._otp, "ui")
            self.sendText("1111", self._otp, "ui")
            print("OTP entered")
        except Exception as e:
            logging.error(f"Mobile login failed: {str(e)}")
            raise e

        # self.clickElement(self._verify_btn, "xpath")
        # print("Click on Verify button")

    def login_gmail(self):
        self.clickElement(self._gmail_icon, "ui")
        print("Click on Gmail Icon")

        self.clickElement(self._gmail_select, "xpath")
        print("Select gmail")


