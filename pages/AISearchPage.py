import time

import logging
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class AISearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _ai_search = 'new UiSelector().resourceId("search_tabbar_button")'

    def ai_tabbar(self):
        self.clickElement(self._ai_search, "ui")
        print("Click on AI Search tab")

