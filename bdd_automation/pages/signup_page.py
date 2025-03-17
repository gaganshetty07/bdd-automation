from selenium.webdriver.common.by import By
from bdd_automation.pages.base_page import BasePage


class SignUpPage(BasePage):
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    SIGN_UP_BUTTON = (By.XPATH, "//button[@title='Create an Account']")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "message-success")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://magento.softwaretestingboard.com/customer/account/create/")

    def enter_registration_details(self, first_name, last_name, email, password):
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.enter_text(self.CONFIRM_PASSWORD, password)

    def submit_registration(self):
        self.click(self.SIGN_UP_BUTTON)

    def get_success_message(self):
        return self.wait_for_element(self.SUCCESS_MESSAGE).text
