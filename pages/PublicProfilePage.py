import time

import logging
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class PublicProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _share_icon = 'new UiSelector().className("android.widget.ImageView").instance(2)'
    _konnections = 'new UiSelector().resourceId("konnections_button")'
    _konnections_search = 'new UiSelector().className("android.widget.ImageView").instance(0)'
    _reviews = 'new UiSelector().resourceId("review_button")'
    _reviews_5star = 'new UiSelector().resourceId("5 star_chip")'
    _reviews_4star = 'new UiSelector().resourceId("4 star_chip")'
    _reviews_3_and_below_star = 'new UiSelector().resourceId("3 stars and below_chip")'
    _add_to_konnection_icon = 'new UiSelector().resourceId("connect_button")'
    _hamburger_menu = 'new UiSelector().className("android.widget.ImageView").instance(3)'
    _read_more = 'new UiSelector().description(" Read more Button")'
    _show_less = 'new UiSelector().description(" Show less Button")'
    _instant_audio_call_icon = 'new UiSelector().resourceId("konnect_call_button")'
    _instant_video_call_icon = 'new UiSelector().resourceId("konnect_video_button")'
    _chat_icon = 'new UiSelector().resourceId("konnect_chat_button")'
    _book_now_cta = ''
    _audio_call_select = ''
    _video_call_select = ''
    _unfollow = 'new UiSelector().description("Unfollow Rachel Green")'
    _report = 'new UiSelector().description("Report Rachel Green")'
    _block = 'new UiSelector().description("Block Rachel Green")'
    _block_btn = 'new UiSelector().resourceId("unblock_button")'
    _report_opt1 = 'new UiSelector().description("Hate speech or bullying")'
    _report_opt2 = 'new UiSelector().description("Violent or sexual content")'
    _report_opt3 = 'new UiSelector().description("False or misleading content")'
    _report_opt4 = 'new UiSelector().description("Impersonation or fake account")'
    _report_other = 'new UiSelector().description("Other")'
    _report_other_txt = 'new UiSelector().className("android.widget.EditText")'
    _cancel_btn = 'new UiSelector().description("Cancel")'
    _report_btn = 'new UiSelector().description("Report")'
    _insta_tile = 'new UiSelector().resourceId("instagram_tile")'
    _unishorts_tab = 'new UiSelector().resourceId("unishorts_tappable")'
    _services_tab = 'new UiSelector().resourceId("services_tappable")'
    _user_unishorts = 'new UiSelector().resourceId("0_tile")'

    # New user
    _send_request_cta = ''
    _start_a_video_call_cta = 'new UiSelector().description("Start a video call")'
    _start_a_chat = 'new UiSelector().description("Start a chat")'


    def public_profile(self):
        self.clickElement(self._share_icon, "ui")
        print("Click on Share icon")

        self.driver.back()

        self.konnections()

        self.reviews()

        self.clickElement(self._add_to_konnection_icon, "ui")
        print("Click on Add to konnection icon")

        self.clickElement(self._read_more, "ui")
        print("Click on Read more cta to view full introduction")

        self.clickElement(self._show_less, "ui")
        print("Click on Show less cta")

        self.clickElement(self._instant_audio_call_icon, "ui")
        print("Click on Instant audio call icon")

        self.driver.back()

        self.clickElement(self._instant_video_call_icon, "ui")
        print("Click on Instant video call icon")

        self.driver.back()

        self.clickElement(self._chat_icon, "ui")
        print("Click on Chat icon")

        self.driver.back()

        self.clickElement(self._insta_tile, "ui")
        print("Click on Instagram icon to check social media profile")

        time.sleep(3)
        self.driver.back()

        self.clickElement(self._services_tab, "ui")
        print("Click on Services tab")

        self.clickElement(self._unishorts_tab, "ui")
        print("Click on Unishorts tab")

        self.clickElement(self._user_unishorts, "ui")
        print("Click on Snips")

        self.driver.back()

        self.clickElement(self._hamburger_menu, "ui")
        print("Click on Hamburger menu")

        self.clickElement(self._unfollow, "ui")
        print("Click on Unfollow user")

        self.report()

        self.clickElement(self._hamburger_menu, "ui")
        print("Click on Hamburger menu")

        self.clickElement(self._block, "ui")
        print("Click on Block user")

        self.clickElement(self._block_btn, "ui")
        print("Click on Block button")

        self.driver.back()
        self.driver.back()


    def new_public_profile(self):
        self.clickElement(self._services_tab, "ui")
        print("Click on Services tab")

        self.clickElement(self._start_a_chat, "ui")
        print("Click on Start a chat cta")

        self.clickElement(self._unishorts_tab, "ui")
        print("Click on Unishorts tab")

        self.clickElement(self._start_a_video_call_cta, "ui")
        print("Click on Start a video call cta")

    def reviews(self):
        self.clickElement(self._reviews, "ui")
        print("Click on Reviews")

        self.clickElement(self._reviews_5star, "ui")
        print("Click on 5 star Reviews")

        self.clickElement(self._reviews_4star, "ui")
        print("Click on 4 star Reviews")

        self.clickElement(self._reviews_3_and_below_star, "ui")
        print("Click on 3 and below star Reviews")

        self.driver.back()

    def konnections(self):
        self.clickElement(self._konnections, "ui")
        print("Click on Konnections")

        self.clickElement(self._konnections_search, "ui")
        self.sendText("ab", self._konnections_search, "ui")
        print("Search Konnection")

        self.driver.back()
        self.driver.back()

    def report(self):
        self.clickElement(self._hamburger_menu, "ui")
        print("Click on Hamburger menu")

        self.clickElement(self._report, "ui")
        print("Click on Report user")

        self.clickElement(self._cancel_btn, "ui")
        print("Click on Cancel button")

        self.clickElement(self._report, "ui")
        print("Click on Report user")

        self.clickElement(self._report_opt1, "ui")
        self.clickElement(self._report_opt2, "ui")
        self.clickElement(self._report_opt3, "ui")
        self.clickElement(self._report_opt4, "ui")
        self.clickElement(self._report_other, "ui")
        print("Select report option")

        self.clickElement(self._report_other_txt, "ui")
        self.sendText("Report testing!!!", self._report_other_txt, "ui")
        print("Enter report reason")

        # self.clickElement(self._report_btn, "ui")
        # print("Click on Report button")
        self.clickElement(self._cancel_btn, "ui")
        print("Click on Cancel button")


