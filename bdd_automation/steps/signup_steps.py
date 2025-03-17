import os
import time
from behave import given, when, then
from selenium import webdriver
from bdd_automation.pages.signup_page import SignUpPage
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

@given("I am on the Magento registration page")
def step_open_signup_page(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=options)
    context.page = SignUpPage(context.driver)

@when("I enter valid registration details")
def step_enter_registration_details(context):
    unique_email = f"test{int(time.time())}@gmail.com"
    context.page.enter_registration_details("John", "Doe", unique_email, Config.VALID_PASSWORD)
    context.unique_email = unique_email

@when("I enter an already registered email")
def step_enter_existing_email(context):
    context.page.enter_registration_details("John", "Doe", Config.VALID_EMAIL, Config.VALID_PASSWORD)

@when("I submit the registration form")
def step_submit_form(context):
    context.page.submit_registration()

@then("I should see a success message")
def step_verify_success(context):
    take_screenshot(context, "signup_success")
    assert "Thank you for registering" in context.page.get_success_message()
    context.driver.quit()

@then("I should see a registration error message")
def step_verify_registration_error(context):
    take_screenshot(context, "signup_error")
    assert "already exists" in context.page.get_error_message()
    context.driver.quit()
