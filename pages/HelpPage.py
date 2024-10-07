import time

import logging
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class HelpPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _help = 'new UiSelector().resourceId("help_tabbar_button")'
    _help_mobile = 'new UiSelector().description("Click to call")'
    _help_banner = 'new UiSelector().description("Learn More")'
    _your_sessions = 'new UiSelector().description("Your sessions")'
    _generate_discount_code = 'new UiSelector().description("Generate discount code")'
    _show_more_availability_status = 'new UiSelector().description("+ Show more")'


    def help_tabbar(self):
        self.clickElement(self._help, "ui")
        print("Click on Help tab")

    def help_actions(self):
        self.clickElement(self._help_mobile, "ui")
        print("Click on Help mobile no")
        self.driver.back()
        self.driver.back()

        self.clickElement(self._help_banner, "ui")
        print("Click on banner")
        self.driver.back()

        self.clickElement(self._your_sessions, "ui")
        print("View your sessions")
        self.driver.back()

        self.clickElement(self._generate_discount_code, "ui")
        print("View discount codes")
        self.driver.back()

        self.scrollToElement(self._show_more_availability_status, "ui")
        self.clickElement(self._show_more_availability_status, "ui")
        print("View availability status")
        self.driver.back()


