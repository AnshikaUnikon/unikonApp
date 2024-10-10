import time

import logging
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _home = 'new UiSelector().resourceId("home_tabbar_button")'
    _categories_view_more = 'new UiSelector().resourceId("view_more_tile")'
    _careers_category = 'new UiSelector().resourceId("careers_tile")'
    _konnections_view_all = 'new UiSelector().resourceId("view_all")'
    _view_user_profile = 'new UiSelector().resourceId("konnect_user_card")'

    # Filters
    _search_bar = 'new UiSelector().resourceId("search_textfield")'
    _filter = 'new UiSelector().resourceId("filter_button")'
    _reset_btn = 'new UiSelector().resourceId("reset_button")'
    _submit_btn = 'new UiSelector().resourceId("submit_button")'
    _categories_dropdown = 'new UiSelector().resourceId("select_industry_dropdown")'
    _careers_filter = 'new UiSelector().resourceId("careers_tile")'
    _topic_dropdown = 'new UiSelector().resourceId("search_textfield")'
    _job_hunting_filter = 'new UiSelector().resourceId("job_hunting_chip")'
    _instantly_available_filter = 'new UiSelector().resourceId("instantly_available_tile")'
    _unikon_verified_filter = 'new UiSelector().resourceId("unikon_verified_tile")'
    _top_rated_filter = 'new UiSelector().resourceId("rating_tile")'
    _discount_applicable_filter = 'new UiSelector().resourceId("offers_tile")'
    _experience_slider = 'new UiSelector().description("0%").instance(0)'
    _age_range_slider = 'new UiSelector().description("0%").instance(1)'
    _gender_dropdown = 'new UiSelector().resourceId("select_gender_dropdown")'
    _female_filter = 'new UiSelector().resourceId("female_tile")'
    _exclude_konnection_filter = 'new UiSelector().resourceId("exclude_konnections_tile")'
    _company_filter = 'new UiSelector().resourceId("company_textfield")'

    # Mini user profile card
    _add_to_konnection_icon = 'new UiSelector().resourceId("connect_button")'
    _audio_call_icon = 'new UiSelector().resourceId("konnect_call_button")'
    _video_call_icon = 'new UiSelector().resourceId("konnect_video_button")'
    _chat_icon = 'new UiSelector().resourceId("konnect_chat_button")'

    # Instant session book
    _book_a_slot_btn = 'new UiSelector().resourceId("book_a_slot_button")'
    _slot_15_min = 'new UiSelector().resourceId("15_tile")'
    _date_select = 'new UiSelector().description("31, Thursday, October 31, 2024")'
    _time1_select = 'new UiSelector().resourceId("0_15_button")'
    _time2_select = 'new UiSelector().resourceId("0_30_button")'
    _book_session_btn = 'new UiSelector().resourceId("book_session_button")'
    _view_offers_cta = 'new UiSelector().resourceId("book_session_button")'
    _apply_btn = 'new UiSelector().description("Apply")'
    _call_purpose = 'new UiSelector().resourceId("call_purpose_textfield")'
    _schedule_btn = 'new UiSelector().resourceId("schedule_button")'

    # Chat initiation
    _text_bar = 'new UiSelector().className("android.widget.EditText")'
    _send_icon = 'new UiSelector().className("android.widget.ImageView").instance(3)'
    _send_message_btn = 'new UiSelector().resourceId("send_message_button")'
    _confirm_btn = 'new UiSelector().resourceId("continue_button")'



    def home_tabbar(self):
        self.clickElement(self._home, "ui")
        print("Click on Home tab")

    def categories(self):
        self.clickElement(self._categories_view_more, "ui")
        print("Click on View more cta for categories")

        self.clickElement(self._careers_category, "ui")
        print("Click on Careers category")

        self.driver.back()
        self.driver.back()

    def filters(self):
        self.scrollToElement(self._konnections_view_all, "ui")
        self.clickElement(self._konnections_view_all, "ui")
        print("Click on View all cta for all konnections")

        self.clickElement(self._search_bar, "ui")
        self.sendText("ab", self._search_bar, "ui")

        self.clickElement(self._filter, "ui")
        print("Click on Filter icon")

        self.clickElement(self._categories_dropdown, "ui")
        print("Click on Categories dropdown")

        self.clickElement(self._careers_filter, "ui")
        print("Click on Careers filter from categories")

        self.clickElement(self._submit_btn, "ui")
        print("Click on Submit button")

        self.clickElement(self._filter, "ui")
        print("Click on Filter icon")

        self.clickElement(self._reset_btn, "ui")
        print("Click on Reset button")

        self.clickElement(self._topic_dropdown, "ui")
        self.sendText("job hunting", self._topic_dropdown, "ui")
        self.clickElement(self._job_hunting_filter, "ui")
        print("Click on Job hunting filter from topics")

        self.clickElement(self._submit_btn, "ui")
        print("Click on Submit button")

        self.clickElement(self._filter, "ui")
        print("Click on Filter icon")

        self.clickElement(self._reset_btn, "ui")
        print("Click on Reset button")

        self.clickElement(self._instantly_available_filter, "ui")
        print("Click on Instantly available filter")

        self.clickElement(self._submit_btn, "ui")
        print("Click on Submit button")

        self.clickElement(self._filter, "ui")
        print("Click on Filter icon")

        self.clickElement(self._reset_btn, "ui")
        print("Click on Reset button")

        self.clickElement(self._unikon_verified_filter, "ui")
        print("Click on Unikon verified filter")

        self.clickElement(self._submit_btn, "ui")
        print("Click on Submit button")

        self.clickElement(self._filter, "ui")
        print("Click on Filter icon")

        self.clickElement(self._reset_btn, "ui")
        print("Click on Reset button")

        self.clickElement(self._top_rated_filter, "ui")
        print("Click on Top rated filter")

        self.clickElement(self._submit_btn, "ui")
        print("Click on Submit button")

        self.clickElement(self._filter, "ui")
        print("Click on Filter icon")

        self.clickElement(self._reset_btn, "ui")
        print("Click on Reset button")

        self.clickElement(self._discount_applicable_filter, "ui")
        print("Click on Discount applicable filter")

        self.clickElement(self._submit_btn, "ui")
        print("Click on Submit button")

        self.clickElement(self._filter, "ui")
        print("Click on Filter icon")

        self.clickElement(self._reset_btn, "ui")
        print("Click on Reset button")

        self.scrollToElement(self._gender_dropdown, "ui")
        self.clickElement(self._gender_dropdown, "ui")
        self.clickElement(self._female_filter, "ui")
        print("Click on Female filter filter from gender dropdown")

        self.clickElement(self._submit_btn, "ui")
        print("Click on Submit button")

        self.clickElement(self._filter, "ui")
        print("Click on Filter icon")

        self.clickElement(self._reset_btn, "ui")
        print("Click on Reset button")

        self.scrollToElement(self._exclude_konnection_filter, "ui")
        self.clickElement(self._exclude_konnection_filter, "ui")
        print("Click on Exclude konnection filter")

        self.clickElement(self._submit_btn, "ui")
        print("Click on Submit button")

        self.clickElement(self._filter, "ui")
        print("Click on Filter icon")

        self.clickElement(self._reset_btn, "ui")
        print("Click on Reset button")

        self.scrollToElement(self._company_filter, "ui")
        self.clickElement(self._company_filter, "ui")
        self.sendText("Unikon", self._company_filter, "ui")
        print("Add Unikon in company filter")

        self.clickElement(self._submit_btn, "ui")
        print("Click on Submit button")

        self.clickElement(self._filter, "ui")
        print("Click on Filter icon")

        self.clickElement(self._reset_btn, "ui")
        print("Click on Reset button")

        self.clickElement(self._submit_btn, "ui")
        print("Click on Submit button")

    def mini_user_profile_card(self):

        self.scrollToElement(self._konnections_view_all, "ui")
        self.clickElement(self._konnections_view_all, "ui")
        print("Click on View all cta for all konnections")



        # Audio call session
        self.clickElement(self._search_bar, "ui")
        self.sendText("rachel", self._search_bar, "ui")

        self.clickElement(self._add_to_konnection_icon, "ui")
        print("Click on Add to konnecton icon")

        self.clickElement(self._audio_call_icon, "ui")
        print("Click on Audio call icon")

        self.clickElement(self._book_a_slot_btn, "ui")
        print("Click on Book a slot button")

        self.clickElement(self._slot_15_min, "ui")
        print("Select 15 min slot")

        self.clickElement(self._date_select, "ui")
        print("Select date")

        self.clickElement(self._time1_select, "ui")
        print("Select time")

        self.clickElement(self._book_session_btn, "ui")
        print("Click on Book session button")

        self.scrollToElement(self._view_offers_cta, "ui")
        self.clickElement(self._view_offers_cta, "ui")
        print("Click on View offer cta")

        if self.isDisplayed(self._apply_btn, "ui"):
            self.clickElement(self._apply_btn, "ui")
            print("Click on Apply button")

        else:
            self.driver.back()

        self.scrollToElement(self._call_purpose, "ui")
        self.clickElement(self._call_purpose, "ui")
        self.sendText("I want to learn more about QA", self._call_purpose, "ui")

        self.clickElement(self._schedule_btn, "ui")
        print("Click on Schedule button")

        time.sleep(3)

        self.driver.back()

        # Video call session
        self.scrollToElement(self._konnections_view_all, "ui")
        self.clickElement(self._konnections_view_all, "ui")
        print("Click on View all cta for all konnections")

        self.clickElement(self._search_bar, "ui")
        self.sendText("rachel", self._search_bar, "ui")

        self.clickElement(self._add_to_konnection_icon, "ui")
        print("Click on Add to konnecton icon")

        self.clickElement(self._video_call_icon, "ui")
        print("Click on Video call icon")

        self.clickElement(self._book_a_slot_btn, "ui")
        print("Click on Book a slot button")

        self.clickElement(self._slot_15_min, "ui")
        print("Select 15 min slot")

        self.clickElement(self._date_select, "ui")
        print("Select date")

        self.clickElement(self._time2_select, "ui")
        print("Select time")

        self.clickElement(self._book_session_btn, "ui")
        print("Click on Book session button")

        self.scrollToElement(self._view_offers_cta, "ui")
        self.clickElement(self._view_offers_cta, "ui")
        print("Click on View offer cta")

        if self.isDisplayed(self._apply_btn, "ui"):
            self.clickElement(self._apply_btn, "ui")
            print("Click on Apply button")

        else:
            self.driver.back()

        self.scrollToElement(self._call_purpose, "ui")
        self.clickElement(self._call_purpose, "ui")
        self.sendText("I want to learn more about QA", self._call_purpose, "ui")

        self.clickElement(self._schedule_btn, "ui")
        print("Click on Schedule button")

        time.sleep(3)

        self.driver.back()

        # Chat
        self.scrollToElement(self._konnections_view_all, "ui")
        self.clickElement(self._konnections_view_all, "ui")
        print("Click on View all cta for all konnections")

        self.clickElement(self._search_bar, "ui")
        self.sendText("tanya", self._search_bar, "ui")

        self.clickElement(self._chat_icon, "ui")
        print("Click on Chat icon")

        self.clickElement(self._confirm_btn, "ui")
        print("Click on Confirm button")

        self.clickElement(self._text_bar, "ui")
        self.sendText("Hi, How are you?", self._text_bar, "ui")

        self.clickElement(self._send_icon, "ui")
        print("Click on Send icon")

        self.clickElement(self._send_message_btn, "ui")
        print("Click on Send button")

        self.clickElement(self._confirm_btn, "ui")
        print("Click on Confirm button")


    def view_public_profile(self, user_name):
        self.scrollToElement(self._konnections_view_all, "ui")
        self.clickElement(self._konnections_view_all, "ui")
        print("Click on View all cta for all konnections")

        self.clickElement(self._search_bar, "ui")
        self.sendText(user_name, self._search_bar, "ui")

        self.clickElement(self._view_user_profile, "ui")


        
        
        


