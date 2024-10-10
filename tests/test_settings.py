import time
import unittest
import pytest
from base.DriverClass import Driver
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.MyProfilePage import MyProfilePage
from pages.SettingsPage import SettingsPage
from pages.AISearchPage import AISearchPage
from pages.HomePage import HomePage
from pages.AppWalkthrough import AppWalkthrough


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class AppWalkthroughTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObject(self):
        self.loginPage = LoginPage(self.driver)
        self.basePage = BasePage(self.driver)
        self.myProfilePage = MyProfilePage(self.driver)
        self.settingsPage = SettingsPage(self.driver)
        self.aiSearchPage = AISearchPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.appWalkthrough = AppWalkthrough(self.driver)

    @pytest.mark.run(order=1)
    def test_launchApp(self):
        self.loginPage.launch_app()

    @pytest.mark.run(order=2)
    def test_visit_profile(self):
        self.appWalkthrough.skip()
        self.myProfilePage.profile_tabbar()
        self.loginPage.login_gmail()
        self.myProfilePage.profile_tabbar()
        self.appWalkthrough.skip()

    @pytest.mark.run(order=3)
    def test_settings(self):
        self.settingsPage.settings_icon()
        self.settingsPage.add_update_bank_details("Kunal Jasrotia", "50100565551482", "HDFC0001669", "CDRPJ1744A")
        self.settingsPage.withdraw_money("100")
        self.settingsPage.add_money("150")
        self.settingsPage.discount_codes("10", "DCSERVICE", "Joey", "DCINSTANT")
        self.settingsPage.referral_code()
        self.settingsPage.create_a_service_card("Test Service", "100", "Learn more about testing")
        self.settingsPage.my_services()
        self.settingsPage.upcoming_sessions()
        self.settingsPage.manage_availability()
        self.settingsPage.recorded_sessions()
        self.settingsPage.recorded_unishorts()
        self.settingsPage.data_privacy()
        self.settingsPage.terms_and_conditions()
        self.settingsPage.payment_policy()
        self.settingsPage.blocked_users()
        self.settingsPage.faqs("sessions")
        self.settingsPage.report_an_issue("Test report an issue")
        self.settingsPage.access_settings()



