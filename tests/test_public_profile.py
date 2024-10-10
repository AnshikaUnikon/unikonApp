import time
import unittest
import pytest
from base.DriverClass import Driver
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.MyProfilePage import MyProfilePage
from pages.UniShortsPage import UniShortsPage
from pages.AISearchPage import AISearchPage
from pages.HomePage import HomePage
from pages.AppWalkthrough import AppWalkthrough
from pages.PublicProfilePage import PublicProfilePage


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class PublicProfileTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObject(self):
        self.loginPage = LoginPage(self.driver)
        self.basePage = BasePage(self.driver)
        self.myProfilePage = MyProfilePage(self.driver)
        self.publicProfilePage = PublicProfilePage(self.driver)
        self.aiSearchPage = AISearchPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.appWalkthrough = AppWalkthrough(self.driver)

    @pytest.mark.run(order=1)
    def test_launchApp(self):
        self.loginPage.launch_app()

    @pytest.mark.run(order=2)
    def test_homeWalkthrough(self):
        self.appWalkthrough.skip()
        self.myProfilePage.profile_tabbar()
        self.loginPage.login_gmail()

    @pytest.mark.run(order=3)
    def test_publicProfile(self):
        self.homePage.view_public_profile("Rachel")
        self.publicProfilePage.public_profile()
        self.homePage.view_public_profile("Joey")
        self.publicProfilePage.new_public_profile()


