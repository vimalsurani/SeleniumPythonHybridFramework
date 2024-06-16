from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    first_name_textbox_id = "input-firstname"
    last_name_textbox_id = "input-lastname"
    register_email_address_textbox_id = "input-email"
    telephone_textbox_id = "input-telephone"
    register_password_textbox_id = "input-password"
    confirm_password_textbox_id = "input-confirm"
    agree_checkbox_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    subscribe_yes_radio_button_xpath = "//input[@name='newsletter'][@value='1']"
    duplicate_email_warning_message_xpath = "//div[@id='account-register']/div[1]"
    agree_privacy_policy_warning_message_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_address_warning_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_xpath = "//input[@id='input-password']/following-sibling::div"

    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID ,self.first_name_textbox_id).click()
        self.driver.find_element(By.ID, self.first_name_textbox_id).clear()
        self.driver.find_element(By.ID, self.first_name_textbox_id).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.last_name_textbox_id).click()
        self.driver.find_element(By.ID, self.last_name_textbox_id).clear()
        self.driver.find_element(By.ID, self.last_name_textbox_id).send_keys(last_name)

    def enter_register_email_address(self, email_address):
        self.driver.find_element(By.ID, self.register_email_address_textbox_id).click()
        self.driver.find_element(By.ID, self.register_email_address_textbox_id).clear()
        self.driver.find_element(By.ID, self.register_email_address_textbox_id).send_keys(email_address)

    def enter_telephone_number(self, telephone):
        self.driver.find_element(By.ID, self.telephone_textbox_id).click()
        self.driver.find_element(By.ID, self.telephone_textbox_id).clear()
        self.driver.find_element(By.ID, self.telephone_textbox_id).send_keys(telephone)

    def enter_register_password(self, password):
        self.driver.find_element(By.ID, self.register_password_textbox_id).click()
        self.driver.find_element(By.ID, self.register_password_textbox_id).clear()
        self.driver.find_element(By.ID, self.register_password_textbox_id).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.ID, self.confirm_password_textbox_id).click()
        self.driver.find_element(By.ID, self.confirm_password_textbox_id).clear()
        self.driver.find_element(By.ID, self.confirm_password_textbox_id).send_keys(confirm_password)

    def select_agree_checkbox(self):
        self.driver.find_element(By.NAME, self.agree_checkbox_name).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def select_yes_radio_button(self):
        self.driver.find_element(By.XPATH, self.subscribe_yes_radio_button_xpath).click()

    def retrieve_duplicate_email_warning_message(self):
        return self.driver.find_element(By.XPATH, self.duplicate_email_warning_message_xpath).text

    def retrieve_agree_privacy_policy_warning_message(self):
        return self.driver.find_element(By.XPATH, self.agree_privacy_policy_warning_message_xpath).text

    def retrieve_first_name_warning_message(self):
        return self.driver.find_element(By.XPATH,self.first_name_warning_xpath).text

    def retrieve_last_name_warning_message(self):
        return self.driver.find_element(By.XPATH,self.last_name_warning_xpath).text

    def retrieve_email_address_warning_message(self):
        return self.driver.find_element(By.XPATH,self.email_address_warning_xpath).text

    def retrieve_telephone_warning_message(self):
        return self.driver.find_element(By.XPATH,self.telephone_warning_xpath).text

    def retrieve_password_warning_message(self):
        return self.driver.find_element(By.XPATH,self.password_warning_xpath).text












