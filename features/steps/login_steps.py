from behave import given, when, then
from selenium import webdriver
from features.pages.login_page import LoginPage

@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.sailor.clothing/login")
    context.login_page = LoginPage(context.driver)

@when('I enter valid email and password')
def step_impl(context):
    context.login_page.enter_credentials("test-----@gmail.com", "trtyry")

@when('I enter invalid email and password')
def step_impl(context):
    context.login_page.enter_credentials("invalid_email@example.com", "invalidpassword")

@when('I click the login button')
def step_impl(context):
    context.login_page.click_login_button()

@when('I click the login button without entering credentials')
def step_impl(context):
    context.login_page.enter_credentials("", "")
    context.login_page.click_login_button()

@then('I should be redirected to the account page')
def step_impl(context):
    expected_title = "Sailor | Sailing Life"
    actual_title = context.login_page.get_page_title()
    assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"

@then('I should see an error message')
def step_impl(context):
    error_message = None
    try:
        error_message = context.login_page.get_error_message()
    except Exception:
        pass

    if not error_message:
        try:
            error_message = context.login_page.get_empty_fields_error()
        except Exception:
            pass

    assert error_message in ["User not found", "Unauthorized"], f"Unexpected error message: '{error_message}'"

@then('I should quit the browser')
def step_impl(context):
    context.driver.quit()
