import time
import unittest
import pytest
from base.DriverClass import Driver
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.ProfilePage import ProfilePage
from pages.UniShortsPage import UniShortsPage
from pages.AISearchPage import AISearchPage
from pages.HomePage import HomePage
from pages.AppWalkthrough import AppWalkthrough


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class AppWalkthroughTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObject(self):
        self.loginPage = LoginPage(self.driver)
        self.basePage = BasePage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.uniShortsPage = UniShortsPage(self.driver)
        self.aiSearchPage = AISearchPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.appWalkthrough = AppWalkthrough(self.driver)

    @pytest.mark.run(order=1)
    def test_launchApp(self):
        self.loginPage.launch_app()

    @pytest.mark.run(order=2)
    def test_homeWalkthrough(self):
        self.appWalkthrough.next()
        self.appWalkthrough.next()
        self.appWalkthrough.next()
        self.appWalkthrough.next()
        self.appWalkthrough.next()
        self.appWalkthrough.cross()
        self.basePage.backGesture()

        self.profilePage.profile_tabbar()
        self.loginPage.login_gmail()

    @pytest.mark.run(order=3)
    def test_home(self):
        # self.homePage.categories()
        # self.homePage.filters()
        self.homePage.mini_user_profile_card()

