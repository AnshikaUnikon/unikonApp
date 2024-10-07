import time
import unittest
import pytest
from base.DriverClass import Driver
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.ProfilePage import ProfilePage
from pages.UniShortsPage import UniShortsPage
from pages.AISearchPage import AISearchPage
from pages.HelpPage import HelpPage
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
        self.helpPage = HelpPage(self.driver)
        self.appWalkthrough = AppWalkthrough(self.driver)

    @pytest.mark.run(order=1)
    def test_launchApp(self):
        self.loginPage.launch_app()

    # @pytest.mark.run(order=2)
    # def test_appWalkthrough(self):
    #     # Home page
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.cross()
    #     self.basePage.backGesture()
    #
    #     # Unishorts page
    #     self.uniShortsPage.unishorts_tabbar()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.cross()
    #
    #     # AI Search page
    #     self.aiSearchPage.ai_tabbar()
    #     self.appWalkthrough.cross()
    #
    #     # Help page
    #     self.helpPage.help_tabbar()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.help_cross()
    #
    #     # Profile page
    #     self.profilePage.profile_tabbar()
    #     self.loginPage.login_gmail()
    #     self.profilePage.profile_tabbar()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.next()
    #     self.appWalkthrough.cross()


    @pytest.mark.run(order=2)
    def test_appWalkthrough_skip(self):
        # Home page
        self.appWalkthrough.skip()

        # Unishorts page
        self.uniShortsPage.unishorts_tabbar()
        self.appWalkthrough.skip()

        # AI Search page
        self.aiSearchPage.ai_tabbar()
        self.appWalkthrough.cross()

        # Help page
        self.helpPage.help_tabbar()
        self.appWalkthrough.skip()

        # Profile page
        self.profilePage.profile_tabbar()
        self.loginPage.login_gmail()
        self.profilePage.profile_tabbar()
        self.appWalkthrough.skip()