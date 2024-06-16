from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from pages.AccountSuccessPage import AccountSuccessPage
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:

    def test_register_with_required_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_down_menu()
        home_page.select_login_option()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("Vimal")
        register_page.enter_last_name("Patel")
        register_page.enter_register_email_address(self.generate_email_with_timestamp())
        register_page.enter_telephone_number("1234567890")
        register_page.enter_register_password("123456")
        register_page.enter_confirm_password("123456")
        register_page.select_agree_checkbox()
        register_page.click_on_continue_button()
        account_success_page = AccountSuccessPage(self.driver)
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_down_menu()
        home_page.select_login_option()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("Vimal")
        register_page.enter_last_name("Patel")
        register_page.enter_register_email_address(self.generate_email_with_timestamp())
        register_page.enter_telephone_number("1234567890")
        register_page.enter_register_password("123456")
        register_page.enter_confirm_password("123456")
        register_page.select_yes_radio_button()
        register_page.select_agree_checkbox()
        register_page.click_on_continue_button()
        account_success_page = AccountSuccessPage(self.driver)
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_down_menu()
        home_page.select_login_option()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("Vimal")
        register_page.enter_last_name("Patel")
        register_page.enter_register_email_address("vimalpatel7449@gmail.com")
        register_page.enter_telephone_number("1234567890")
        register_page.enter_register_password("123456")
        register_page.enter_confirm_password("123456")
        register_page.select_yes_radio_button()
        register_page.select_agree_checkbox()
        register_page.click_on_continue_button()
        expected_warning_text = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_warning_message().__contains__(expected_warning_text)

    def test_without_entering_any_field(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_down_menu()
        home_page.select_login_option()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("")
        register_page.enter_last_name("")
        register_page.enter_register_email_address("")
        register_page.enter_telephone_number("")
        register_page.enter_register_password("")
        register_page.enter_confirm_password("")
        register_page.click_on_continue_button()
        expected_privacy_policy_warning_text = "Warning: You must agree to the Privacy Policy!"
        assert register_page.retrieve_agree_privacy_policy_warning_message().__contains__(expected_privacy_policy_warning_text)
        expected_first_name_warning_text = "First Name must be between 1 and 32 characters!"
        assert register_page.retrieve_first_name_warning_message().__eq__(expected_first_name_warning_text)
        expected_last_name_warning_text = "Last Name must be between 1 and 32 characters!"
        assert register_page.retrieve_last_name_warning_message().__eq__(expected_last_name_warning_text)
        expected_email_warning_text = "E-Mail Address does not appear to be valid!"
        assert register_page.retrieve_email_address_warning_message().__eq__(expected_email_warning_text)
        expected_telephone_warning_text = "Telephone must be between 3 and 32 characters!"
        assert register_page.retrieve_telephone_warning_message().__eq__(expected_telephone_warning_text)
        expected_password_warning_text = "Password must be between 4 and 20 characters!"
        assert register_page.retrieve_password_warning_message().__eq__(expected_password_warning_text)

    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return "vimal" + time_stamp + "@gmail.com"
