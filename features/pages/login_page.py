from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # XPath selectors
        self.email_field = (By.XPATH, "//input[@class='form-control' and @type='email']")
        self.password_field = (By.XPATH, "//input[@placeholder='Password']")
        self.login_button = (By.XPATH, "//button[normalize-space()='Login Now']")
        self.logout_link = (By.XPATH, "//a[normalize-space()='Logout']")
        self.error_message = (By.XPATH, "//div[contains(text(),'User not found')]")
        self.empty_fields_error = (By.XPATH, "//div[contains(text(),'Unauthorized')]")
        self.page_title_after_login = "Sailor | Sailing Life"

    def enter_credentials(self, email, password):
        """Clear and enter email and password into the respective fields."""
        self.driver.find_element(*self.email_field).clear()
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        """Click the login button if it is clickable, with proper timeout handling."""
        try:
            wait = WebDriverWait(self.driver, 10)  # 10 seconds timeout
            button = wait.until(EC.element_to_be_clickable(self.login_button))
            button.click()
        except TimeoutException:
            print("Login button was not clickable within the timeout period.")
            return False
        return True

    def get_page_title(self):
        """Get the title of the current page."""
        return self.driver.title

    def is_logout_link_visible(self):
        """Check if the logout link is visible on the page (indicating successful login)."""
        try:
            return self.driver.find_element(*self.logout_link).is_displayed()
        except:
            return False  # Return False if element is not found

    def get_error_message(self):
        """Get the error message for invalid login."""
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.error_message)
            )
            return element.text
        except TimeoutException:
            return ""

    def get_empty_fields_error(self):
        """Get the error message when login fields are empty."""
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.empty_fields_error)
            )
            return element.text
        except TimeoutException:
            return ""

    def verify_login_successful(self):
        """Verify that the login was successful by checking the page title."""
        if self.driver.title == self.page_title_after_login:
            return True
        return False
