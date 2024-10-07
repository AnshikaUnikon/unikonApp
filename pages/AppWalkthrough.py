import time

import logging
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class AppWalkthrough(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _next_btn = 'new UiSelector().resourceId("next_step")'
    _skip_cta = 'new UiSelector().resourceId("skip_walkthrough_button")'
    _cross_icon = 'new UiSelector().className("android.widget.Button")'
    _help_cross_icon = 'new UiSelector().className("android.widget.Button").instance(4)'

    def next(self):
        self.clickElement(self._next_btn, "ui")
        print("Click on next button")

    def skip(self):
        self.clickElement(self._skip_cta, "ui")
        print("Click on skip button")

    def cross(self):
        self.clickElement(self._cross_icon, "ui")
        print("Click on cross icon")

    def help_cross(self):
        self.clickElement(self._help_cross_icon, "ui")
        print("Click on cross icon")
