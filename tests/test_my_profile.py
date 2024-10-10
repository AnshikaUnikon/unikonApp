import unittest
import pytest
from base.DriverClass import Driver
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.MyProfilePage import MyProfilePage


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ProfileTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObject(self):
        self.loginPage = LoginPage(self.driver)
        self.myProfilePage = MyProfilePage(self.driver)

    @pytest.mark.run(order=1)
    def test_launchApp(self):
        self.loginPage.launch_app()

    @pytest.mark.run(order=2)
    def test_loginGmail(self):
        self.loginPage.login_gmail()

    @pytest.mark.run(order=3)
    def test_updateProfile(self):
        # self.myProfilePage.update_details()
        self.myProfilePage.edit_details()

    # @pytest.mark.run(order=4)
    # def test_myProfile(self):
    #     self.myProfilePage.my_profile()
