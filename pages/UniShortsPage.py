import time

import logging
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class UniShortsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _unishorts = 'new UiSelector().resourceId("unitube_tabbar_button")'

    def unishorts_tabbar(self):
        self.clickElement(self._unishorts, "ui")
        print("Click on Home tab")

