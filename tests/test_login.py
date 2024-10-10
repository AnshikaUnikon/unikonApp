import unittest
import pytest
from base.DriverClass import Driver
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.MyProfilePage import MyProfilePage
from pages.AppWalkthrough import AppWalkthrough


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObject(self):
        self.loginPage = LoginPage(self.driver)
        self.myProfilePage = MyProfilePage(self.driver)
        self.appWalkthrough = AppWalkthrough(self.driver)

    @pytest.mark.run(order=1)
    def test_launchApp(self):
        self.loginPage.launch_app()

    @pytest.mark.run(order=2)
    def test_appWalkthrough(self):
        self.appWalkthrough.cross()

    # @pytest.mark.run(order=3)
    # def test_mobileNoLogin(self):
    #     self.myProfilePage.profile_tabbar()
    #     self.loginPage.login_mobile_no()

    @pytest.mark.run(order=3)
    def test_loginGmail(self):
        self.myProfilePage.profile_tabbar()
        self.loginPage.login_gmail()
