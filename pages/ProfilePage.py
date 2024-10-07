import time
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _profile = 'new UiSelector().resourceId("profile_tabbar_button")'

    #Edit Profile
    _profile_screen = '//android.view.View[@content-desc="Profile"]'
    _edit_icon = '//android.widget.ScrollView/android.view.View[5]'
    _add_profile_image_icon = '//android.widget.ScrollView/android.widget.ImageView[1]'
    _add_profile_image_btn = '2'
    _gallery_icon = '//android.widget.ImageView[@content-desc="Gallery"]'
    # _while_using_the_app = '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'
    _device_gallery = '(//android.widget.ImageView[@resource-id="com.android.intentresolver:id/icon"])[1]'
    _download_gallery = '(//android.widget.ImageView[@resource-id="com.sec.android.gallery3d:id/thumbnail"])[5]'
    _image_gallery = '(//android.widget.FrameLayout[@resource-id="com.sec.android.gallery3d:id/deco_view_layout"])[1]'
    _check_icon = '//android.widget.Button[@content-desc="Crop"]'
    _first_name = '//android.widget.EditText[@text="Shreya"]'
    _add_first_name = '//android.widget.ScrollView/android.view.View[3]/android.widget.EditText'
    _last_name = '//android.widget.EditText[@text="Singhal"]'
    _add_last_name = '//android.widget.ScrollView/android.view.View[4]/android.widget.EditText'
    _designation = '//android.widget.ScrollView/android.view.View[5]/android.widget.EditText'
    _edit_designation = '//android.widget.EditText[@text="QA Automation Engg."]'
    _link = '//android.widget.ScrollView/android.widget.EditText[1]'
    _edit_link = '//android.widget.EditText[@text="https://unikon.ai/"]'
    _link_display_name = '//android.widget.ScrollView/android.widget.EditText[2]'
    _edit_link_display_name = '//android.widget.EditText[@text="UnikonAi"]'
    _work_experience = '//android.widget.ScrollView/android.view.View[7]/android.widget.EditText'
    _edit_work_experience = '//android.widget.EditText[@text="3"]'
    _add_work_experience = '//android.widget.ScrollView/android.view.View[5]/android.widget.EditText'
    _current_organisation = '//android.widget.ScrollView/android.view.View[6]/android.widget.EditText'
    _edit_current_organisation = '//android.widget.EditText[@text="Unikon.ai"]'
    _add_current_organisation = '//android.widget.ScrollView/android.view.View[4]/android.widget.EditText'
    _city = '//android.widget.ScrollView/android.view.View[5]/android.widget.EditText'
    _edit_city = '//android.widget.EditText[@text="Gurgaon"]'
    _add_city = '//android.widget.ScrollView/android.view.View[3]/android.widget.EditText'
    _select_city = '//android.view.View[@content-desc="Gurgaon"]'
    _edit_select_city = '//android.view.View[@content-desc="Noida"]'
    _edit_about_yourself = '//android.widget.EditText[@text="Hi I can help you with testing queries"]'
    _about_yourself = '//android.widget.ScrollView/android.view.View[4]/android.widget.EditText'
    _calender = '//android.view.View[@content-desc="Choose date"]'
    _edit_calender = '//android.view.View[@content-desc="01/07/2012"]'
    _dob = '//android.widget.Button[@content-desc="1, Sunday, July 1, 2012"]'
    _edit_dob = '//android.widget.Button[@content-desc="2, Monday, July 2, 2012"]'
    _ok_btn = '//android.widget.Button[@content-desc="OK"]'
    _cancel_btn = '//android.widget.Button[@content-desc="Cancel"]'
    _update_btn = '//android.widget.Button[@content-desc="Update"]'

    #Reviews
    _reviews = '//android.widget.Button[@content-desc="0 reviews"]'
    _5_star_reviews = '//android.view.View[@content-desc="5 star"]'
    _4_star_reviews = '//android.view.View[@content-desc="4 star"]'
    _3_star_reviews = '//android.view.View[@content-desc="3 stars and below"]'

    _konnections = '//android.view.View[@content-desc="5 Konnections"]'
    _profile_link = '//android.widget.ImageView[@content-desc="About Unikon"]'

    #Instant services
    _audio_call = '//android.widget.ImageView[@content-desc="₹ 100/hr "]'
    _audio_call1 = '//android.widget.ImageView[@content-desc="₹100 / hr"]'
    _edit_audio_call = '//android.widget.EditText[@text="100"]'
    _add_audio_call = '//android.widget.ScrollView/android.view.View[4]/android.widget.ImageView'
    _video_call = '//android.widget.ImageView[@content-desc="₹ 250/hr "]'
    _video_call1 = '//android.widget.ImageView[@content-desc="₹  250 / hr"]'
    _edit_video_call = '//android.widget.EditText[@text="250"]'
    _add_video_call = '//android.widget.ScrollView/android.view.View[7]/android.widget.ImageView'
    _chats = '//android.widget.ImageView[@content-desc="₹ 1"]'
    _chats1 = '//android.widget.ImageView[@content-desc="₹  1"]'
    _edit_chats = '//android.widget.EditText[@text="1"]'
    _add_chats = '//android.widget.ScrollView/android.view.View[7]/android.widget.ImageView'
    _save_btn = '//android.widget.Button[@content-desc="Save"]'
    _update_price = '//android.view.View[@content-desc="Update your price >"]'

    #Social media
    _social_media_links = '//android.view.View[@content-desc="Social media links: Click to update"]'
    _click_add_link = '(//android.widget.ImageView[@content-desc="Add link"])[1]'
    _linked_in_how = '(//android.view.View[@content-desc="How?"])[1]'
    _add_linked_in = '//android.widget.EditText'
    _click_linked_in = '//android.widget.ImageView[@content-desc="https://www.linkedin.com/in/anshika-srivastava-5707731b1?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"]'
    _remove_linked_in = '//android.widget.EditText[@text="https://www.linkedin.com/in/anshika-srivastava-5707731b1?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"]/android.view.View'
    _insta_how = '(//android.view.View[@content-desc="How?"])[2]'
    _edit_insta = '//android.widget.ScrollView/android.view.View[8]/android.widget.EditText'
    _click_insta = '//android.widget.ImageView[@content-desc="https://www.instagram.com/anshika_srivastava9555?igsh=NTQyNXExNWhsNGtt"]'
    _remove_insta = '//android.widget.EditText[@text="https://www.instagram.com/anshika_srivastava9555?igsh=NTQyNXExNWhsNGtt"]/android.view.View'
    _youtube_how = '(//android.view.View[@content-desc="How?"])[3]'
    _edit_youtube = '//android.widget.ScrollView/android.view.View[9]/android.widget.EditText'
    _click_youtube = '//android.widget.ImageView[@content-desc="https://youtube.com/@safiya?si=_tt_p-X98ApuUwfW"]'
    _remove_youtube = '//android.widget.EditText[@text="https://youtube.com/@safiya?si=_tt_p-X98ApuUwfW"]/android.view.View'
    _twitter_how = '(//android.view.View[@content-desc="How?"])[3]'
    _edit_twitter = '//android.widget.ScrollView/android.view.View[10]/android.widget.EditText'
    _click_twitter = '//android.widget.ImageView[@content-desc="https://x.com/johncena?s=11"]'
    _remove_twitter = '//android.widget.EditText[@text="https://x.com/johncena?s=11"]/android.view.View'
    _facebook_how = '(//android.view.View[@content-desc="How?"])[4]'
    _edit_facebook = '//android.widget.ImageView[@content-desc="Add link"]'
    _add_facebook = '//android.widget.ScrollView/android.view.View[10]/android.widget.EditText'
    _click_facebook = '//android.widget.ImageView[@content-desc="https://www.facebook.com/JenniferAniston?mibextid=ZbWKwL"]'
    _remove_facebook = '//android.widget.EditText[@text="https://www.facebook.com/JenniferAniston?mibextid=ZbWKwL"]/android.view.View'
    _add_links = '//android.widget.ScrollView/android.view.View[7]/android.widget.EditText'

    #Sessions
    _sessions = '//android.view.View[@content-desc="Sessions"]'
    _past_sessions = '//android.view.View[@content-desc="Past"]'
    _upcoming_sessions = '//android.view.View[@content-desc="Upcoming"]'

    _inspirations = '//android.widget.ImageView[@content-desc="Inspirations"]'
    _no_results_found = '//android.view.View[@content-desc="No result found"]'

    #Availability status and Schedule
    _set_schedule = '//android.view.View[@content-desc="Availability status Offline Set schedule "]'
    _add_more_slots_btn = '//android.widget.Button[@content-desc="Add more slots"]'
    _time_drop_down_1 = '//android.view.View[@content-desc="Set your availability * Please add the time slots Select days * Please select the days All week"]/android.widget.Button[1]'
    _start_time_1 = '//android.view.View[@content-desc="12:00 AM"]'
    _time_drop_down_2 = '//android.view.View[@content-desc="Set your availability * Please add the time slots Select days * Please select the days All week"]/android.widget.Button[2]'
    _end_time_1 = '//android.view.View[@content-desc="1:30 AM"]'
    _all_week_slide_btn = '//android.view.View[@content-desc="Set your availability * Please add the time slots Select days * All week"]/android.view.View[2]'
    _monday = '//android.view.View[@content-desc="M"]'
    _friday = '//android.view.View[@content-desc="F"]'
    _add_btn = '//android.widget.Button[@content-desc="Add"]'
    _close_btn = '//android.widget.Button[@content-desc="Close"]'
    _edit_schedule_btn = '//android.view.View[@content-desc="12:00 AM - 1:30 AM Tue, Wed, Thu, Sat, Sun"]/android.widget.ImageView[2]'
    _time_drop_down_3 = '//android.widget.Button[@content-desc="12:00 AM"]'
    _start_time_2 = '//android.view.View[@content-desc="12:15 AM"]'
    _end_time_2 = '//android.view.View[@content-desc="1:15 AM"]'
    _delete_schedule_btn = '//android.view.View[@content-desc="12:15 AM - 1:15 AM Tue, Wed, Thu, Fri, Sat, Sun"]/android.widget.ImageView[1]'
    _on_availability_status_slide_btn = '//android.widget.ScrollView/android.view.View[5]'
    _continue_btn = '//android.widget.Button[@content-desc="Continue"]'
    _appear_on_top_slide = '(//android.widget.Switch[@resource-id="android:id/switch_widget"])[9]'
    _off_availability_status_slide_btn = '//android.widget.ScrollView/android.view.View[6]'
    _update_your_calendar = '//android.view.View[@content-desc="Update your Calendar Add more slots"]'
    _confirm_btn = '//android.widget.Button[@content-desc="Confirm"]'

    #Dashboard -> Earnings
    _dashboard = '//android.view.View[@content-desc="Dashboard"]'
    _earnings = '//android.view.View[@content-desc="₹ 0 Your overall earnings"]'
    _withdraw_money_btn = '//android.view.View[@content-desc="Withdraw money"]'
    _unishows_earnings = '//android.view.View[@content-desc="UniShows"]'
    _sessions_earnings = '//android.view.View[@content-desc="Sessions"]'
    _instant_audio_call_earnings = '//android.view.View[@content-desc="Instant Audio Call"]'
    _instant_video_call_earnings = '//android.view.View[@content-desc="Instant Video Call"]'
    _instant_message_earnings = '//android.view.View[@content-desc="Instant Message"]'

    # Dashboard -> UniWallet
    _uniwallet = '//android.view.View[@content-desc="UniWallet"]'
    _withdraw_btn = '//android.widget.Button[@content-desc="Withdraw"]'
    _account_update_btn = '//android.view.View[@content-desc="Update"]'
    _amount = '//android.widget.EditText'
    _confirm_withdrawal_btn = '//android.widget.Button[@content-desc="Confirm withdrawal"]'
    _add_money_btn = '//android.widget.Button[@content-desc="Add money"]'
    _100rs = '//android.widget.Button[@content-desc="₹ 100"]'
    _200rs = '//android.widget.Button[@content-desc="₹ 200"]'
    _500rs = '//android.widget.Button[@content-desc="₹ 500"]'
    _netbanking = '//android.widget.TextView[@text="Yes Bank Netbanking"]'
    _success_btn = '//android.widget.Button[@text="Success"]'
    _transaction_history = '//android.view.View[@content-desc="Transaction History"]'
    _acc_name_1 = '//android.widget.EditText[@text="Kunal Jasrotia"]'
    _acc_number_1 = '(//android.widget.EditText[@text="50100565551482"])[1]'
    _confirm_acc_number_1 = '(//android.widget.EditText[@text="50100565551482"])[2]'
    _ifsc_code_1 = '//android.widget.EditText[@text="HDFC0001669"]'
    _pan_1 = '//android.widget.EditText[@text="CDRPJ1744A"]'
    _acc_name_2 = '//android.widget.ScrollView/android.view.View[1]/android.widget.EditText'
    _acc_number_2 = '//android.widget.ScrollView/android.view.View[2]/android.widget.EditText'
    _confirm_acc_number_2 = '//android.widget.ScrollView/android.view.View[3]/android.widget.EditText'
    _ifsc_code_2 = '//android.widget.ScrollView/android.view.View[4]/android.widget.EditText'
    _pan_2 = '//android.widget.ScrollView/android.view.View[4]/android.widget.EditText'
    _update_bank_details_btn = '//android.widget.Button[@content-desc="Update bank details"]'

    # Dashboard -> UniShows
    _unishows = '//android.view.View[@content-desc="UniShows"]'
    _live_unishows = '//android.view.View[@content-desc="Live"]'
    _past_unishows = '//android.view.View[@content-desc="Past"]'
    _upcoming_unishows = '//android.view.View[@content-desc="Upcoming"]'

    # Dashboard -> Call history
    _call_history = '//android.view.View[@content-desc="Call history"]'
    _missed_calls = '//android.view.View[@content-desc="Missed Tab 2 of 2"]'

    _referral_code = '//android.view.View[@content-desc="Referral code"]'
    _reviews_dashboard = '//android.view.View[@content-desc="Reviews"]'

    #Services
    _services = '//android.view.View[@content-desc="Services"]'
    _add_service_btn = '//android.widget.Button[@content-desc="Add Service"]'
    _service_title_1 = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.widget.EditText'
    _add_service_title = '//android.widget.EditText'
    _service_type_drop_down_1 = '//android.view.View[@content-desc="Type of service Select"]'
    _video_call_service = '//android.widget.RadioButton[@content-desc="Video Call"]'
    _audio_call_service = '//android.widget.RadioButton[@content-desc="Audio Call"]'
    _service_duration_drop_down_1 = '//android.view.View[@content-desc="Set duration Select"]'
    _service_duration_1 = '//android.widget.RadioButton[@content-desc="10 Minutes"]'
    _service_amount_1 = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[5]/android.widget.EditText'
    _upload_video = '//android.widget.ImageView[@content-desc="Upload video"]'
    _select_video = '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[5]'
    _create_btn = '//android.widget.Button[@content-desc="Create"]'
    _edit_service = '//android.widget.Button[@content-desc="Edit"]'
    _service_title_2 = '//android.widget.EditText[@text="Test"]'
    _service_type_drop_down_2 = '//android.view.View[@content-desc="Type of service Audio Call"]'
    _service_duration_drop_down_2 = '//android.view.View[@content-desc="Set duration 10 Minutes"]'
    _service_duration_2 = '//android.widget.RadioButton[@content-desc="15 Minutes"]'
    _service_amount_field = '//android.widget.EditText[@text="50"]'
    _service_amount_2 = '//android.widget.ScrollView/android.view.View[4]/android.widget.EditText'
    _remove_video_icon = '//android.widget.Button[@content-desc="Close"]'
    _delete_btn = '//android.widget.Button[@content-desc="Delete"]'

    _services_profile = '//android.view.View[@content-desc="Services Tab 2 of 3"]'
    _unishows_profile = '//android.view.View[@content-desc="Unishows Tab 3 of 3"]'


    def profile_tabbar(self):
        self.clickElement(self._profile, "ui")
        print("Click on My Profile tab")

    def update_details(self):
        self.clickElement(self._profile_screen, "xpath")
        print("Click on Profile Screen")

        self.clickElement(self._edit_icon, "xpath")
        print("Click on Edit icon")

        self.clickElement(self._designation, "xpath")
        self.sendText("QA Automation Engg.", self._designation, "xpath")
        print("Designation entered")

        self.driver.back()
        self.clickElement(self._link, "xpath")
        self.sendText("https://unikon.ai/", self._link, "xpath")
        print("Profile Link entered")

        self.clickElement(self._link_display_name, "xpath")
        self.sendText("UnikonAi", self._link_display_name, "xpath")
        print("Link Display Name entered")

        self.driver.back()
        self.clickElement(self._work_experience, "xpath")
        self.sendText("3", self._add_work_experience, "xpath")
        print("Work Experience entered")

        self.driver.back()
        self.clickElement(self._current_organisation, "xpath")
        self.sendText("Unikon.ai", self._add_current_organisation, "xpath")
        print("Current Organisation entered")

        self.driver.back()
        self.clickElement(self._city, "xpath")
        self.sendText("Gurgaon", self._add_city, "xpath")
        print("City entered")

        self.driver.back()
        self.clickElement(self._select_city, "xpath")
        print("Select City")

        self.clickElement(self._about_yourself, "xpath")
        self.sendText("Hi I can help you with testing queries", self._about_yourself, "xpath")
        print("About me entered")

        self.driver.back()
        self.clickElement(self._calender, "xpath")
        print("Click on Calender icon")

        self.clickElement(self._dob, "xpath")
        print("Click on DOB icon")

        self.clickElement(self._ok_btn, "xpath")
        print("Click on Ok button")

        self.waitForElement(self._update_btn, "scroll")
        self.clickElement(self._update_btn, "xpath")
        print("Click on Update button")

#Edit
    def edit_details(self):
        self.clickElement(self._profile_screen, "xpath")
        print("Click on Profile Screen")

        self.clickElement(self._edit_icon, "xpath")
        print("Click on Edit icon")

        self.clickElement(self._add_profile_image_icon, "xpath")
        print("Click on Add profile image icon")

        # self.clickElement(self._add_profile_image_btn, "index")
        # print("Click on Add profile image button")

        self.clickElement(self._gallery_icon, "xpath")
        print("Click on Gallery icon")

        self.clickElement(self._device_gallery, "xpath")
        print("Click on Device Gallery icon")

        self.clickElement(self._download_gallery, "xpath")
        print("Click on Download option")

        self.clickElement(self._image_gallery, "xpath")
        print("Select Profile picture")

        self.clickElement(self._check_icon, "xpath")
        print("Click on Check icon")

        self.clickElement(self._first_name, "xpath")
        self.clearElement(self._first_name, "xpath")
        self.sendText("Anshika", self._add_first_name, "xpath")
        print("First Name entered")

        self.clickElement(self._last_name, "xpath")
        self.clearElement(self._last_name, "xpath")
        self.sendText("Srivastava", self._add_last_name, "xpath")
        print("Last Name entered")

        self.clickElement(self._edit_designation, "xpath")
        self.clearElement(self._edit_designation, "xpath")
        self.sendText("QA Engg.", self._designation, "xpath")
        print("Designation entered")

        self.driver.back()
        self.clickElement(self._edit_link, "xpath")
        self.clearElement(self._edit_link, "xpath")
        self.sendText(
            "https://m.economictimes.com/tech/funding/unikon-ai-raises-2-million-in-funding-led-by-zerodhas-nikhil-kamath-others/articleshow/111127998.cms",
            self._link, "xpath")
        print("Profile Link entered")

        self.clickElement(self._edit_link_display_name, "xpath")
        self.clearElement(self._edit_link_display_name, "xpath")
        self.sendText("About Unikon", self._link_display_name, "xpath")
        print("Link Display Name entered")

        self.driver.back()
        self.clickElement(self._edit_work_experience, "xpath")
        self.clearElement(self._edit_work_experience, "xpath")
        self.sendText("5", self._add_work_experience, "xpath")
        print("Work Experience entered")

        self.driver.back()
        self.clickElement(self._edit_current_organisation, "xpath")
        self.clearElement(self._edit_current_organisation, "xpath")
        self.sendText("UNIKON", self._add_current_organisation, "xpath")
        print("Current Organisation entered")

        self.driver.back()
        self.clickElement(self._edit_city, "xpath")
        self.clearElement(self._edit_city, "xpath")
        self.sendText("Noida", self._add_city, "xpath")
        print("City entered")

        self.driver.back()
        self.clickElement(self._edit_select_city, "xpath")
        print("Select City")

        self.clickElement(self._edit_about_yourself, "xpath")
        self.clearElement(self._edit_about_yourself, "xpath")
        self.sendText("Any testing queries? ASK ME!!!", self._about_yourself, "xpath")
        print("About me entered")

        self.driver.back()
        self.clickElement(self._edit_calender, "xpath")
        print("Click on Calender icon")

        self.clickElement(self._cancel_btn, "xpath")
        print("Click on Cancel button")

        self.clickElement(self._calender, "xpath")
        print("Click on Calender icon")

        self.clickElement(self._edit_dob, "xpath")
        print("Click on DOB icon")

        self.clickElement(self._ok_btn, "xpath")
        print("Click on Ok button")

        self.waitForElement(self._update_btn, "scroll")
        self.clickElement(self._update_btn, "xpath")
        print("Click on Update button")

    def my_profile(self):
        self.clickElement(self._profile_screen, "xpath")
        print("Click on Profile Screen")

        self.clickElement(self._reviews, "xpath")
        print("Click on Reviews")

        self.reviews()

        self.driver.back()
        self.clickElement(self._konnections, "xpath")
        print("Click on Konnections")

        self.driver.back()
        self.clickElement(self._profile_link, "xpath")
        print("Click on Profile Link")

        self.driver.back()
        self.clickElement(self._audio_call, "xpath")
        print("Click on Audio call icon")

        self.driver.back()
        self.clickElement(self._video_call, "xpath")
        print("Click on Video call icon")

        self.driver.back()
        self.clickElement(self._chats, "xpath")
        print("Click on Reviews")

        self.driver.back()
        self.clickElement(self._update_price, "xpath")
        print("Click on Update your price")

        # self.update_price()

        self.driver.back()
        self.clickElement(self._social_media_links, "xpath")
        print("Click on Social media links")

        self.add_social_media_links()

        self.remove_social_media_links()

        self.clickElement(self._sessions, "xpath")
        print("Click on Sessions")

        self.sessions()

        self.clickElement(self._inspirations, "xpath")
        print("Click on Inspirations")

        self.driver.back()
        self.waitForElement(self._no_results_found, "scroll")

        self.clickElement(self._set_schedule, "xpath")
        print("Click on Inspirations")

        self.set_schedule()

        self.driver.back()
        self.clickElement(self._on_availability_status_slide_btn, "xpath")
        print("Click on Availability status slide button")

        self.clickElement(self._continue_btn, "xpath")
        print("Click on Continue button")

        self.clickElement(self._appear_on_top_slide, "xpath")
        print("Click on Appear on top slide button")

        self.driver.back()
        self.clickElement(self._off_availability_status_slide_btn, "xpath")
        print("Click on Availability status slide button")

        self.clickElement(self._update_your_calendar, "xpath")
        print("Click on Update your calendar")

        self.driver.back()
        self.clickElement(self._confirm_btn, "xpath")
        print("Click on Confirm button")

        self.clickElement(self._dashboard, "xpath")
        print("Click on Dashboard")

        self.clickElement(self._earnings, "xpath")
        print("Click on Your overall earnings")

        self.earnings()

        self.driver.back()
        self.clickElement(self._uniwallet, "xpath")
        print("Click on UniWallet")

        self.driver.back()
        self.clickElement(self._sessions, "xpath")
        print("Click on Sessions")

        self.sessions()

        self.driver.back()
        self.clickElement(self._unishows, "xpath")
        print("Click on UniShows")

        self.unishows()

        self.driver.back()
        self.clickElement(self._call_history, "xpath")
        print("Click on Call history")

        self.call_history()

        self.driver.back()
        self.clickElement(self._referral_code, "xpath")
        print("Click on Referral code")

        self.driver.back()
        self.clickElement(self._transaction_history, "xpath")
        print("Click on Transaction history")

        self.driver.back()
        self.clickElement(self._reviews_dashboard, "xpath")
        print("Click on Reviews")

        self.reviews()

        self.driver.back()
        self.driver.back()
        self.clickElement(self._uniwallet, "xpath")
        print("Click on UniWallet")

        self.uniwallet()

        self.driver.back()
        self.driver.back()

        self.clickElement(self._services, "xpath")
        print("Click on Services")

        self.services()

        self.driver.back()

        self.clickElement(self._services_profile, "xpath")
        print("Click on Services on profile")

        self.clickElement(self._unishows_profile, "xpath")
        print("Click on Unishows on profile")


    def reviews(self):
        self.clickElement(self._5_star_reviews, "xpath")
        self.clickElement(self._4_star_reviews, "xpath")
        self.clickElement(self._3_star_reviews, "xpath")

    def update_price(self):
        self.clickElement("android.widget.ImageView", "class", 5)
        self.clickElement(self._edit_audio_call, "xpath")
        self.clearElement(self._edit_audio_call, "xpath")
        self.sendText("200", self._add_audio_call, "xpath")
        print("Audio Call price added")

        self.driver.back()
        self.clickElement(self._video_call1, "xpath")
        self.clickElement(self._edit_video_call, "xpath")
        self.clearElement(self._edit_video_call, "xpath")
        self.sendText("500", self._add_video_call, "xpath")
        print("Video Call price added")

        self.driver.back()
        self.clickElement(self._chats1, "xpath")
        self.clickElement(self._edit_chats, "xpath")
        self.clearElement(self._edit_chats, "xpath")
        self.sendText("100", self._add_chats, "xpath")
        print("Chat price added")

        self.driver.back()
        self.clickElement(self._save_btn, "xpath")
        print("Click on Save button")

    def add_social_media_links(self):
        self.clickElement(self._linked_in_how, "xpath")
        print("Click on How for Linkedin")
        time.sleep(2)

        self.driver.back()
        self.clickElement(self._click_add_link, "xpath")
        self.sendText(
            "https://www.linkedin.com/in/anshika-srivastava-5707731b1?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
            self._add_linked_in, "xpath")
        print("Linkedin link added")

        self.driver.back()
        self.clickElement(self._insta_how, "xpath")
        print("Click on How for Instagram")
        time.sleep(2)

        self.driver.back()
        self.clickElement(self._click_add_link, "xpath")
        self.clickElement(self._edit_insta, "xpath")
        self.sendText("https://www.instagram.com/anshika_srivastava9555?igsh=NTQyNXExNWhsNGtt", self._edit_insta,
                      "xpath")
        print("Instagram link added")

        self.driver.back()
        self.clickElement(self._youtube_how, "xpath")
        print("Click on How for Youtube")
        time.sleep(2)

        self.driver.back()
        self.clickElement(self._click_add_link, "xpath")
        self.clickElement(self._edit_youtube, "xpath")
        self.sendText("https://youtube.com/@safiya?si=_tt_p-X98ApuUwfW", self._add_links, "xpath")
        print("Youtube link added")

        self.driver.back()
        self.clickElement(self._twitter_how, "xpath")
        print("Click on How for Twitter")
        time.sleep(2)

        self.driver.back()
        self.clickElement(self._click_add_link, "xpath")
        self.clickElement(self._edit_twitter, "xpath")
        self.sendText("https://x.com/johncena?s=11", self._add_links, "xpath")
        print("Twitter link added")

        self.driver.back()
        self.clickElement(self._facebook_how, "xpath")
        print("Click on How for Facebook")
        time.sleep(2)

        self.driver.back()
        self.clickElement(self._edit_facebook, "xpath")
        self.clickElement(self._add_facebook, "xpath")
        self.sendText("https://www.facebook.com/JenniferAniston?mibextid=ZbWKwL", self._add_links, "xpath")
        print("Facebook link added")

        self.driver.back()
        self.clickElement(self._save_btn, "xpath")
        print("Click on Save button")

    def remove_social_media_links(self):
        self.clickElement(self._click_linked_in, "xpath")
        self.clickElement(self._remove_linked_in, "xpath")
        print("Linkedin link removed")

        self.clickElement(self._click_insta, "xpath")
        self.clickElement(self._remove_insta, "xpath")
        print("Instagram link removed")

        self.clickElement(self._click_youtube, "xpath")
        self.clickElement(self._remove_youtube, "xpath")
        print("Youtube link removed")

        self.clickElement(self._click_twitter, "xpath")
        self.clickElement(self._remove_twitter, "xpath")
        print("Twitter link removed")

        self.clickElement(self._click_facebook, "xpath")
        self.clickElement(self._remove_facebook, "xpath")
        print("Facebook link removed")

        self.clickElement(self._save_btn, "xpath")
        print("Click on Save button")

    def sessions(self):
        self.clickElement(self._past_sessions, "xpath")
        print("Click on Past Sessions")

        self.clickElement(self._upcoming_sessions, "xpath")
        print("Click on Upcoming Session")
        self.driver.back()

    def set_schedule(self):
        time.sleep(4)
        self.clickElement(self._add_more_slots_btn, "xpath")
        print("Click on Add more slots button")

        self.clickElement(self._time_drop_down_1, "xpath")
        self.clickElement(self._start_time_1, "xpath")

        self.clickElement(self._time_drop_down_2, "xpath")
        self.clickElement(self._end_time_2, "xpath")

        self.clickElement(self._all_week_slide_btn, "xpath")

        self.clickElement(self._monday, "xpath")
        self.clickElement(self._friday, "xpath")

        self.clickElement(self._add_btn, "xpath")
        print("New schedule added")

        self.clickElement(self._close_btn, "xpath")

        self.clickElement(self._edit_schedule_btn, "xpath")
        print("Click on edit icon")

        self.clickElement(self._time_drop_down_3, "xpath")
        self.clickElement(self._start_time_2, "xpath")

        self.clickElement(self._time_drop_down_2, "xpath")
        self.clickElement(self._end_time_2, "xpath")

        self.clickElement(self._friday, "xpath")

        self.clickElement(self._update_btn, "xpath")

        self.clickElement(self._delete_schedule_btn, "xpath")

    def earnings(self):
        self.clickElement(self._withdraw_money_btn, "xpath")
        print("Click on Withdraw money button")

        self.driver.back()
        self.clickElement(self._unishows_earnings, "xpath")
        print("Click on Unishow earnings")

        self.clickElement(self._sessions_earnings, "xpath")
        print("Click on Sessions earnings")

        self.clickElement(self._instant_audio_call_earnings, "xpath")
        print("Click on Instant audio call earnings")

        self.swipeLeftToRight()
        self.clickElement(self._instant_video_call_earnings, "xpath")
        print("Click on Instant video call earnings")

        self.clickElement(self._instant_message_earnings, "xpath")
        print("Click on Instant message earnings")

    def unishows(self):
        self.clickElement(self._live_unishows, "xpath")
        print("Click on Live Booked Unishows")

        self.clickElement(self._past_unishows, "xpath")
        print("Click on Past Booked Unishows")

        self.clickElement(self._upcoming_unishows, "xpath")
        print("Click on Upcoming Booked Unishows")

    def call_history(self):
        self.clickElement(self._missed_calls, "xpath")
        print("Click on Missed calls")

    def uniwallet(self):
        #Withdraw
        self.clickElement(self._withdraw_btn, "xpath")
        print("Click on Withdraw button")

        self.clickElement(self._amount, "xpath")
        self.sendText("100", self._amount, "xpath")
        print("Enter amount to withdraw")

        self.driver.back()
        self.waitForElement(self._confirm_withdrawal_btn, "scroll")
        self.clickElement(self._confirm_withdrawal_btn, "xpath")
        print("Click on Confirm withdrawal button")

        #Add Money
        self.clickElement(self._add_money_btn, "xpath")
        print("Click on Add money button")

        self.clickElement(self._500rs, "xpath")
        print("Click on 500")

        self.clickElement(self._200rs, "xpath")
        print("Click on 200")

        self.clickElement(self._100rs, "xpath")
        print("Click on 100")

        self.clickElement(self._confirm_btn, "xpath")
        print("Click on Confirm button")

        self.clickElement(self._netbanking, "xpath")
        print("Click on Netbanking")

        self.clickElement(self._success_btn, "xpath")
        print("Click on Success button")

        self.clickElement(self._close_btn, "xpath")
        print("Click on Close button")

        #transaction history
        self.clickElement(self._transaction_history, "xpath")
        print("Click on Transaction history")
        self.driver.back()

        #Add bank details
        self.clickElement(self._account_update_btn, "xpath")
        print("Click on Update you account button")

        self.clickElement(self._acc_name_1, "xpath")
        self.clearElement(self._acc_name_1, "xpath")
        self.sendText("Kunal Jasrotia", self._acc_name_2, "xpath")
        print("User Name entered")

        self.clickElement(self._acc_number_1, "xpath")
        self.clearElement(self._acc_number_1, "xpath")
        self.sendText("50100565551482", self._acc_number_2, "xpath")
        print("Account number entered")

        self.driver.back()
        self.clickElement(self._confirm_acc_number_1, "xpath")
        self.clearElement(self._confirm_acc_number_1, "xpath")
        self.sendText("50100565551482", self._confirm_acc_number_2, "xpath")
        print("Account number entered")

        self.driver.back()
        self.clickElement(self._ifsc_code_1, "xpath")
        self.clearElement(self._ifsc_code_1, "xpath")
        self.sendText("HDFC0001669", self._ifsc_code_2, "xpath")
        print("IFSC code entered")

        self.driver.back()
        self.clickElement(self._pan_1, "xpath")
        self.clearElement(self._pan_1, "xpath")
        self.sendText("CDRPJ1744A", self._pan_2, "xpath")
        print("PAN entered")

        self.driver.back()
        self.clickElement(self._update_bank_details_btn, "xpath")
        print("Click on Update bank details button")

    def services(self):
        #Create Service
        self.clickElement(self._add_service_btn, "xpath")
        print("Click on Add service button")

        self.clickElement(self._service_title_1, "xpath")
        self.sendText("Test", self._add_service_title, "xpath")
        print("Service title entered")

        self.clickElement(self._service_type_drop_down_1, "xpath")
        print("Click on Service type drop down")

        self.clickElement(self._audio_call_service, "xpath")
        print("Select audio call service")

        self.clickElement(self._service_duration_drop_down_1, "xpath")
        print("Click on Service duration drop down")

        self.clickElement(self._service_duration_1, "xpath")
        print("Select Service duration")

        self.driver.back()
        self.clickElement(self._service_amount_1, "xpath")
        self.sendText("50", self._service_amount_2, "xpath")
        print("Service amount entered")

        self.driver.back()
        self.clickElement(self._upload_video, "xpath")
        self.clickElement(self._gallery_icon, "xpath")
        self.clickElement(self._select_video, "xpath")
        time.sleep(5)

        self.waitForElement(self._create_btn, "scroll")
        self.clickElement(self._create_btn, "xpath")

        #Edit Service
        self.clickElement(self._edit_service, "xpath")
        print("Click on Edit service button")

        self.clickElement(self._service_title_2, "xpath")
        self.sendText("_1", self._service_title_2, "xpath")
        print("Service title entered")

        self.clickElement(self._service_type_drop_down_2, "xpath")
        print("Click on Service type drop down")

        self.clickElement(self._video_call_service, "xpath")
        print("Select Video call service")

        self.clickElement(self._service_duration_drop_down_2, "xpath")
        print("Click on Service duration drop down")

        self.clickElement(self._service_duration_2, "xpath")
        print("Select Service duration")

        self.driver.back()
        self.clickElement(self._service_amount_field, "xpath")
        self.clearElement(self._service_amount_field, "xpath")
        self.sendText("100", self._service_amount_2, "xpath")
        print("Service amount entered")

        self.driver.back()
        self.clickElement(self._remove_video_icon, "xpath")

        self.clickElement(self._save_btn, "xpath")
        print("Click on Save button")

        #Delete Service
        self.clickElement(self._edit_service, "xpath")
        print("Click on Edit service button")

        self.clickElement(self._delete_btn, "xpath")
        print("Click on Delete service button")


