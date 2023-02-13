from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    USER_NAME = (By.CSS_SELECTOR, "input[id='user_login-873']")
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='first_name-873']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='last_name-873']")
    EMAIL = (By.CSS_SELECTOR, "input[id='user_email-873']")
    PASSWORD = (By.CSS_SELECTOR, "input[id='user_password-873']")
    REPEAT_PASSWORD = (By.CSS_SELECTOR, "input[id='confirm_user_password-873']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "input[id='um-submit-btn']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[class='um-button um-alt']")
    CHECK_USER_NAME_HEADER = (By.CSS_SELECTOR, "div[class='besclwp-page-title'] h1")
    CHECK_USER_NAME_IN_THE_PROFILE = (By.CSS_SELECTOR, "div[class='um-name'] a")


