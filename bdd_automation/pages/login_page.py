from selenium.webdriver.common.by import By
from bdd_automation.pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    LOGIN_BUTTON = (By.ID, "send2")
    ERROR_MESSAGE = (By.CLASS_NAME, "message-error")
    WELCOME_MESSAGE = (By.XPATH, "//span[contains(text(), 'Welcome')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://magento.softwaretestingboard.com/customer/account/login/")

    def enter_login_details(self, email, password):
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)

    def submit_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.wait_for_element(self.ERROR_MESSAGE).text

    def get_welcome_message(self):
        return self.wait_for_element(self.WELCOME_MESSAGE).text
