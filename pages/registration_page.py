from generator.generator import *
from pages.base_page import *
from locators.registration_locators import *


class RegistrationPage(BasePage):
    locators = RegistrationPageLocators
    @allure.step('Fill all fields correct data')
    def fill_all_fields_correct_data(self):
        person_info = next(generated_person())
        user_name = person_info.user_name
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        password = person_info.password
        self.element_is_visible(self.locators.USER_NAME).send_keys(user_name)
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.REPEAT_PASSWORD).send_keys(password)
        # self.element_is_visible(self.locators.REGISTER_BUTTON).click()