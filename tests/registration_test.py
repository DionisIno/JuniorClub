import time
from pages.registration_page import *


@allure.suite('Registration page')
class TestRegistration:
    @allure.feature('Correct registration data')
    class TestCorrectRegistrationData:
        @allure.title('Enter correct data in the registration fields')
        def test_input_correct_data(self, driver):
            registration_page = RegistrationPage(driver, "https://junioritclub.com/signup")
            registration_page.open()
            username = registration_page.fill_all_fields_correct_data()
            first_username, second_username = registration_page.check_filled_form()
            time.sleep(5)
            print(username)
            print(first_username)
            print(second_username)