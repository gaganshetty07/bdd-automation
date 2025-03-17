import os
import time
from behave import given, when, then
from selenium import webdriver
from bdd_automation.pages.login_page import LoginPage
from bdd_automation.utils.config import Config

# Ensure screenshots directory exists
SCREENSHOTS_DIR = "screenshots"
if not os.path.exists(SCREENSHOTS_DIR):
    os.makedirs(SCREENSHOTS_DIR)

def take_screenshot(context, name):
    """Wait and capture screenshot"""
    time.sleep(2)  # Allow time for page to fully load
    if context.driver:
        file_path = os.path.join(SCREENSHOTS_DIR, f"{name}.png")
        context.driver.save_screenshot(file_path)
        print(f"Screenshot saved: {file_path}")
    else:
        print("WebDriver is not active. Screenshot not taken.")

@given("I am on the Magento login page")
def step_open_login_page(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=options)
    context.page = LoginPage(context.driver)

@when("I enter valid login credentials")
def step_enter_valid_credentials(context):
    context.page.enter_login_details(Config.VALID_EMAIL, Config.VALID_PASSWORD)

@when("I enter invalid login credentials")
def step_enter_invalid_credentials(context):
    context.page.enter_login_details(Config.INVALID_EMAIL, Config.INVALID_PASSWORD)

@when("I leave the login fields empty")
def step_leave_fields_empty(context):
    context.page.enter_login_details("", "")

@when("I submit the login form")
def step_submit_login_form(context):
    context.page.submit_login()

@then("I should be logged in successfully")
def step_verify_successful_login(context):
    take_screenshot(context, "login_success")
    assert "Welcome" in context.page.get_welcome_message()
    context.driver.quit()

@then("I should see a login error message")
def step_verify_login_error_message(context):
    take_screenshot(context, "login_error")
    assert "Invalid login" in context.page.get_error_message()
    context.driver.quit()

@then("I should see a validation message")
def step_verify_validation_message(context):
    take_screenshot(context, "login_validation_error")
    assert "This is a required field" in context.page.get_error_message()
    context.driver.quit()
