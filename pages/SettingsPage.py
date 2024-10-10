import time

import logging
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class SettingsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _settings_icon = 'new UiSelector().resourceId("setting_button")'

    # Add update bank details
    _add_update_bank_details_tile = 'new UiSelector().resourceId("add_update_bank_details_tile")'
    _account_holder_name_textfield = 'new UiSelector().resourceId("account_holder_name_textfield")'
    _account_number_textfield = 'new UiSelector().resourceId("account_number_textfield")'
    _confirm_account_number_textfield = 'new UiSelector().resourceId("confirm_account_number_textfield")'
    _ifsc_code_textfield = 'new UiSelector().resourceId("ifsc_code_textfield")'
    _pan_number_textfield = 'new UiSelector().resourceId("pan_number_textfield")'
    _update_bank_details_btn = 'new UiSelector().resourceId("update_button")'

    # Withdraw money
    _withdraw_money_tile = 'new UiSelector().resourceId("withdraw_money_tile")'
    _enter_amount_textfield = 'new UiSelector().resourceId("enter_amount_textfield")'
    _confirm_withdrawal_btn = 'new UiSelector().resourceId("confirm_withdrawal_button")'

    # Add money
    _add_money_tile = 'new UiSelector().resourceId("add_money_tile")'
    _transaction_history_cta = 'new UiSelector().resourceId("transaction_history_button")'
    _withdraw_btn = 'new UiSelector().resourceId("withdraw_button")'
    _add_money_btn = 'new UiSelector().resourceId("add_money_button")'
    _100_chip = 'new UiSelector().resourceId("100_chip")'
    _200_chip = 'new UiSelector().resourceId("200_chip")'
    _500_chip = 'new UiSelector().resourceId("500_chip")'
    _continue_btn = 'new UiSelector().resourceId("continue_button")'
    _bank_select = 'new UiSelector().text("Bank of Baroda - Retail Banking Netbanking")'
    _payment_success = 'new UiSelector().text("Success")'
    _payment_failure = 'new UiSelector().text("Failure")'
    _close_btn = 'new UiSelector().description("Close")'

    # Discount codes
    _discount_codes_tile = 'new UiSelector().resourceId("discount_codes_tile")'
    _generate_discount_code_btn = 'new UiSelector().description("Generate code")'
    _service_cards_tile = 'new UiSelector().resourceId("service_cards_service_card")'
    _unikonnect_tile = 'new UiSelector().resourceId("unikonnect_service_card")'
    _service_card_checkbox = 'new UiSelector().resourceId("test_2checkbox")'
    _audio_call_checkbox = 'new UiSelector().resourceId("audio_call_service_card")'
    _select_all_toggle = 'new UiSelector().className("android.view.View").instance(11)'
    _select_more = 'new UiSelector().description("Select more")'
    _select_rate_dropdown = 'new UiSelector().resourceId("select_rate_dropdown")'
    _select_percent = 'new UiSelector().description("10%")'
    _early_bird_toggle = 'new UiSelector().resourceId("availability_switch")'
    _early_bird_textfield = 'new UiSelector().resourceId("make_early_bird_textfield"))'
    _discount_code_textfield = 'new UiSelector().resourceId("discount_code_textfield")'
    _select_validity = 'new UiSelector().resourceId("date_picker")'
    _select_date = 'new UiSelector().description("31, Thursday, October 31, 2024")'
    _ok_cta = 'new UiSelector().description("OK")'
    _add_people_textfield = 'new UiSelector().resourceId("add_people_textfield")'
    _select_people = 'new UiSelector().resourceId("joey_tribbiani_tile")'
    _generate_code_btn = 'new UiSelector().resourceId("generate_code")'
    _share_icon = 'new UiSelector().resourceId("share_button")'
    _share_btn = 'new UiSelector().description("Share")'
    _edit_btn = 'new UiSelector().resourceId("edit_button")'
    _delete_user = 'new UiSelector().resourceId("delete_button").instance(1)'
    _save_btn = 'new UiSelector().resourceId("save_button")'
    _services = 'new UiSelector().resourceId("services_chip")'
    _instant_services = 'new UiSelector().resourceId("instant services_chip")'
    _edit_discount_code = 'new UiSelector().resourceId("edit_button").instance(0)'
    _user_availed_cta = 'new UiSelector().description("1 user availed")'
    _delete_icon = 'new UiSelector().resourceId("delete_button")'
    _confirm_btn = 'new UiSelector().description("Confirm")'

    # Referral code
    _referral_code_tile = 'new UiSelector().resourceId("referral_code_tile")'
    _copy_btn = 'new UiSelector().resourceId("copy_text_button")'

    # Access settings
    _access_settings_tile = 'new UiSelector().resourceId("access_settings_tile")'
    _delete_my_account = 'new UiSelector().resourceId("delete_my_account_tile")'
    _logout = 'new UiSelector().resourceId("logout_tile")'


    # Create a service card
    _create_a_service_card_tile = 'new UiSelector().resourceId("create_a_service_card_tile")'
    _title_textfield = 'new UiSelector().resourceId("title_textfield")'
    _service_dropdown = 'new UiSelector().resourceId("service_textfield")'
    _audio_type = 'new UiSelector().description("Audio Call")'
    _video_type = 'new UiSelector().description("Video Call")'
    _duration_dropdown = 'new UiSelector().resourceId("duration_textfield")'
    _10_min_duration_select = 'new UiSelector().description("10 Minutes")'
    _price_textfield = 'new UiSelector().resourceId("price_textfield")'
    _benefits_textfield = 'new UiSelector().resourceId("benefits_textfield")'
    _upload_cta = 'new UiSelector().resourceId("upload_button")'
    _gallery = 'new UiSelector().description("Gallery"))'
    _video_select = 'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance(0)'

    # My services
    _my_services_tile = 'new UiSelector().resourceId("my_services_tile")'
    _create_more_service_cards_btn = 'new UiSelector().resourceId("add_service_button")'

    # Upcoming sessions
    _upcoming_sessions_tile = 'new UiSelector().resourceId("upcoming_sessions_tile")'
    _past_chip = 'new UiSelector().resourceId("past_chip")'
    _upcoming_chip = 'new UiSelector().resourceId("upcoming_chip")'
    _reschedule_session_btn = 'new UiSelector().resourceId("reschedule_session_button")'
    _select_time = 'new UiSelector().resourceId("10_0_button")'
    _book_session_btn = 'new UiSelector().resourceId("book_session_button")'

    # Manage availability
    _manage_availability_tile = 'new UiSelector().resourceId("manage_availability_tile")")'
    _add_more_slots_btn = 'new UiSelector().description("Add more slots")'
    _start_time = 'new UiSelector().className("android.widget.Button").instance(0)'
    _start_time_select = 'new UiSelector().description("12:00 AM")'
    _end_time = 'new UiSelector().className("android.widget.Button").instance(1)'
    _end_time_select = 'new UiSelector().description("12:15 AM")'
    _all_week_toggle = 'new UiSelector().className("android.view.View").instance(7)'
    _add_btn = 'new UiSelector().description("Add")'
    _edit_service_icon = 'new UiSelector().className("android.widget.ImageView").instance(2)'
    _sunday_select = 'new UiSelector().description("S").instance(0)'
    _monday_select = 'new UiSelector().description("M")'
    _update_btn = 'new UiSelector().description("Update")'
    _delete_service_icon = 'new UiSelector().className("android.widget.ImageView").instance(1)'

    # Recorded sessions
    _recorded_sessions_tile = 'new UiSelector().resourceId("recorded_sessions_tile")'

    # Recorded unishorts
    _recorded_unishorts_tile = 'new UiSelector().resourceId("recorded_unishorts_tile")'

    # Data Privacy
    _data_privacy_tile = 'new UiSelector().resourceId("data_privacy_tile")'

    # T&C
    _terms_conditions_tile = 'new UiSelector().resourceId("terms_conditions_tile")'

    # Payment policy
    _payment_policy_tile = 'new UiSelector().resourceId("payment_policy_tile")'

    # Blocked users
    _blocked_users_tile = 'new UiSelector().resourceId("blocked_users_tile")'
    _unblock_cta = 'new UiSelector().resourceId("unblock_button").instance(0)'
    _unblock_btn = 'new UiSelector().resourceId("unblock_button")'

    # FAQ's
    _faqs_tile = 'new UiSelector().resourceId("faqs_tile")'
    _search_textfield = 'new UiSelector().resourceId("search_textfield")'
    _faq_topic = 'new UiSelector().resourceId("how_much_can_i_charge_for_my_sessions_tile")'
    _report_an_issue_tab = 'new UiSelector().resourceId("report_an_issue_tappable")'

    # Report an issue
    _report_an_issue_tile = 'new UiSelector().resourceId("report_an_issue_tile")'
    _category_dropdown = 'new UiSelector().resourceId("select_dropdown")'
    _category_select = 'new UiSelector().resourceId("profile_tile")'
    _description_textfield = 'new UiSelector().resourceId("description_textfield")'
    _call_us_btn = 'new UiSelector().resourceId("call_now_button")'
    _submit_btn = 'new UiSelector().resourceId("submit_button")'


    def settings_icon(self):
        self.clickElement(self._settings_icon, "ui")
        print("Click on Settings icon")

    def add_update_bank_details(self, account_holder_name, account_number, ifsc_code, pan_number):
        self.clickElement(self._add_update_bank_details_tile, "ui")
        print("Click on Add update bank details tile")

        self.clickElement(self._account_holder_name_textfield, "ui")
        self.clearElement(self._account_holder_name_textfield, "ui")
        self.sendText(account_holder_name, self._account_holder_name_textfield, "ui")
        print("Add account holder name")
        self.driver.back()

        self.clickElement(self._account_number_textfield, "ui")
        self.clearElement(self._account_number_textfield, "ui")
        self.sendText(account_number, self._account_number_textfield, "ui")
        print("Add account number")
        self.driver.back()

        self.clickElement(self._confirm_account_number_textfield, "ui")
        self.clearElement(self._confirm_account_number_textfield, "ui")
        self.sendText(account_number, self._confirm_account_number_textfield, "ui")
        print("Add account number")
        self.driver.back()

        self.clickElement(self._ifsc_code_textfield, "ui")
        self.clearElement(self._ifsc_code_textfield, "ui")
        self.sendText(ifsc_code, self._ifsc_code_textfield, "ui")
        print("Add account holder name")
        self.driver.back()

        self.clickElement(self._pan_number_textfield, "ui")
        self.clearElement(self._pan_number_textfield, "ui")
        self.sendText(pan_number, self._pan_number_textfield, "ui")
        print("Add PAN number")
        self.driver.back()

        self.clickElement(self._update_bank_details_btn, "ui")
        print("Click on Update bank details button")
        time.sleep(7)

    def withdraw_money(self, withdraw_amount):
        self.clickElement(self._withdraw_money_tile, "ui")
        print("Click on Withdraw money tile")

        self.clickElement(self._update_bank_details_btn, "ui")
        print("Click on Update bank details button")
        self.driver.back()

        self.clickElement(self._enter_amount_textfield, "ui")
        self.sendText(withdraw_amount, self._enter_amount_textfield, "ui")
        print("Enter withdraw amount")
        self.driver.back()

        self.scrollToElement(self._confirm_withdrawal_btn, "ui")
        self.clickElement(self._confirm_withdrawal_btn, "ui")
        print("Click on Confirm withdrawal button")

    def add_money(self, add_amount):
        self.clickElement(self._add_money_tile, "ui")
        print("Click on Add money tile")

        self.clickElement(self._update_bank_details_btn, "ui")
        print("Click on Update bank details button")
        self.driver.back()

        self.clickElement(self._transaction_history_cta, "ui")
        print("Click on Transaction history cta")
        self.driver.back()

        self.clickElement(self._withdraw_btn, "ui")
        print("Click on Withdraw button")
        self.driver.back()

        self.clickElement(self._add_money_btn, "ui")
        print("Click on Add money button")

        self.clickElement(self._enter_amount_textfield, "ui")
        self.sendText(add_amount, self._enter_amount_textfield, "ui")
        print("Enter amount to add")

        self.clickElement(self._100_chip, "ui")
        self.clickElement(self._200_chip, "ui")
        self.clickElement(self._500_chip, "ui")
        print("Click on suggested filter chips")

        self.clickElement(self._continue_btn, "ui")
        print("Click on Confirm button")
        time.sleep(7)

        self.clickElement(self._bank_select, "ui")
        print("Select bank")

        self.clickElement(self._payment_success, "ui")
        print("Click on Success")

        self.clickElement(self._close_btn, "ui")
        print("Click on Close button")
        self.driver.back()

    def discount_codes(self, user_count1, discount_code1, user_name1, user_count2, discount_code2, user_name2):
        self.clickElement(self._discount_codes_tile, "ui")
        print("Click on Discount codes tile")

        self.clickElement(self._generate_discount_code_btn, "ui")
        print("Click on Generate code button")

        self.clickElement(self._service_cards_tile, "ui")
        print("Click on Service card")

        self.clickElement(self._service_card_checkbox, "ui")
        print("Click on Service card checkbox")

        self.create_discount_codes(user_count1, discount_code1, user_name1)

        self.edit_discount_codes()

        self.clickElement(self._generate_discount_code_btn, "ui")
        print("Click on Generate code button")

        self.clickElement(self._unikonnect_tile, "ui")
        print("Click on Unikonnect card")

        self.clickElement(self._audio_call_checkbox, "ui")
        print("Click on Audio call checkbox")

        self.create_discount_codes(user_count2, discount_code2, user_name2)

        self.edit_discount_codes()

        self.clickElement(self._services, "ui")
        print("Click on Services suggested filter")

        self.clickElement(self._edit_discount_code, "ui")
        print("Click on Edit button")

        self.clickElement(self._delete_icon, "ui")
        print("Click on Delete icon")

        self.clickElement(self._confirm_btn, "ui")
        print("Click on Confirm button")

        self.clickElement(self._instant_services, "ui")
        print("Click on Instant Services suggested filter")

        self.clickElement(self._edit_btn, "ui")
        print("Click on Edit button")

        self.clickElement(self._delete_icon, "ui")
        print("Click on Delete icon")

        self.clickElement(self._confirm_btn, "ui")
        print("Click on Confirm button")

        for x in range(0, 17):
            self.driver.back()

    def create_discount_codes(self, user_count, discount_code, user_name):
        self.clickElement(self._select_all_toggle, "ui")
        print("Click on Select all toggle")

        self.clickElement(self._continue_btn, "ui")
        print("Click on Continue button")

        self.clickElement(self._select_more, "ui")
        print("Click on Select more cta")

        self.clickElement(self._select_rate_dropdown, "ui")
        print("Click on Select rate dropdown")

        self.clickElement(self._select_percent, "ui")
        print("Select rate")

        self.clickElement(self._early_bird_toggle, "ui")
        print("Click on Early bird toggle")

        self.clickElement(self._early_bird_textfield, "ui")
        self.sendText(user_count, self._early_bird_textfield, "ui")
        print("Enter User count")
        self.driver.back()

        self.clickElement(self._discount_code_textfield, "ui")
        self.sendText(discount_code, self._discount_code_textfield, "ui")
        print("Enter Discount code")
        self.driver.back()

        self.clickElement(self._select_validity, "ui")
        print("Select validity")

        self.clickElement(self._select_date, "ui")
        print("Select date")

        self.clickElement(self._ok_cta, "ui")
        print("Click on Ok cta")

        self.clickElement(self._early_bird_toggle, "ui")
        print("Click on Early bird toggle")

        self.clickElement(self._add_people_textfield, "ui")
        self.sendText(user_name, self._add_people_textfield, "ui")
        self.clickElement(self._select_people, "ui")
        print("Enter user name")
        self.driver.back()

        self.clickElement(self._generate_code_btn, "ui")
        print("Click on Generate code button")

        self.clickElement(self._share_icon, "ui")
        print("Click on Share icon")
        self.driver.back()

        self.clickElement(self._share_btn, "ui")
        print("Click on Share button")
        self.driver.back()

    def edit_discount_codes(self):
        self.clickElement(self._edit_btn, "ui")
        print("Click on Edit button")

        self.scrollToElement(self._delete_user, "ui")
        self.clickElement(self._delete_user, "ui")
        print("Click on delete icon")

        self.clickElement(self._early_bird_toggle, "ui")
        print("Click on Early bird toggle")

        self.clickElement(self._save_btn, "ui")
        print("Click on Save button")

    def referral_code(self):
        self.clickElement(self._referral_code_tile, "ui")
        print("Click on Referral codes tile")

        self.clickElement(self._copy_btn, "ui")
        print("Click on Copy button")
        self.driver.back()

    def access_settings(self):
        self.clickElement(self._access_settings_tile, "ui")
        print("Click on Access settings tile")

        self.clickElement(self._delete_my_account, "ui")
        print("Click on Delete my account")
        self.driver.back()

        self.clickElement(self._logout, "ui")
        print("Click on Logout")

    def create_a_service_card(self, service_card_title, service_price, service_benefits):
        self.clickElement(self._create_a_service_card_tile, "ui")
        print("Click on Create a service card tile")

        self.clickElement(self._title_textfield, "ui")
        self.sendText(service_card_title, self._title_textfield, "ui")
        print("Enter Service card title")
        self.driver.back()

        self.clickElement(self._service_dropdown, "ui")
        print("Click on Service type dropdown")

        self.clickElement(self._audio_type, "ui")
        print("Select service type")

        self.clickElement(self._duration_dropdown, "ui")
        print("Click on Duration dropdown")

        self.clickElement(self._10_min_duration_select, "ui")
        print("Select service duration")

        self.clickElement(self._price_textfield, "ui")
        self.sendText(service_price, self._price_textfield, "ui")
        print("Enter Service price")
        self.driver.back()

        self.clickElement(self._benefits_textfield, "ui")
        self.sendText(service_benefits, self._benefits_textfield, "ui")
        print("Enter Service benefits")
        self.driver.back()

        self.select_video()

        self.scrollToElement(self._save_btn, "ui")
        self.clickElement(self._save_btn, "ui")
        print("Click on Create button")

    def select_video(self):
        self.clickElement(self._upload_cta, "ui")
        print("Click on Upload video")

        self.clickElement(self._gallery, "ui")
        print("Click on Gallery option")

        self.clickElement(self._video_select, "ui")
        print("Select video")

    def my_services(self):
        self.clickElement(self._my_services_tile, "ui")
        print("Click on My services tile")

        self.clickElement(self._create_more_service_cards_btn, "ui")
        print("Click on Create more service cards button")
        self.driver.back()
        self.driver.back()

        # Need to add edit service card code

    def upcoming_sessions(self):
        self.clickElement(self._upcoming_sessions_tile, "ui")
        print("Click on Upcoming sessions tile")

        self.clickElement(self._create_a_service_card_tile, "ui")
        print("Click on Create a service card tile")

        self.clickElement(self._past_chip, "ui")
        print("Click on Past suggested filter")

        self.clickElement(self._upcoming_chip, "ui")
        print("Click on Upcoming suggested filter")

        if self.isDisplayed(self._reschedule_session_btn, "ui"):
            self.clickElement(self._reschedule_session_btn, "ui")
            print("Click on Reschedule session button")

            self.clickElement(self._select_date, "ui")
            print("Select date")

            self.clickElement(self._select_time, "ui")
            print("select time")

            self.clickElement(self._book_session_btn, "ui")
            print("Click on Book session button")

        self.driver.back()

    def manage_availability(self):
        self.scrollToElement(self._manage_availability_tile, "ui")
        self.clickElement(self._manage_availability_tile, "ui")
        print("Click on Manage availability tile")


        self.clickElement(self._service_dropdown, "ui")
        print("Click on Service type dropdown")

        self.clickElement(self._audio_type, "ui")
        print("Select service type")

        self.clickElement(self._duration_dropdown, "ui")
        print("Click on Duration dropdown")

        self.clickElement(self._10_min_duration_select, "ui")
        print("Select service duration")

        self.clickElement(self._price_textfield, "ui")
        self.sendText(service_price, self._price_textfield, "ui")
        print("Enter Service price")
        self.driver.back()

        self.clickElement(self._benefits_textfield, "ui")
        self.sendText(service_benefits, self._benefits_textfield, "ui")
        print("Enter Service benefits")
        self.driver.back()

        self.select_video()

        self.scrollToElement(self._save_btn, "ui")
        self.clickElement(self._save_btn, "ui")
        print("Click on Create button")





        
        
        


