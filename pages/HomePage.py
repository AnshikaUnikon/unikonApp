import time

import logging
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _view_more_category_cta = 'com.android.permissioncontroller:id/permission_allow_button'
    _home = 'new UiSelector().resourceId("home_tabbar_button")'

    def home_tabbar(self):
        self.clickElement(self._home, "ui")
        print("Click on Home tab")

