import time
from pages.registration_page import *


@allure.suite('Registration page')
class TestRegistration:
    @allure.feature('Correct registration data')
    class TestCorrectRegistrationData:
        @allure.title('Enter correct data in the registration fields')
        def test_correct_data(self, driver):
            registration_page = RegistrationPage(driver, "https://junioritclub.com/signup")
            registration_page.open()
            registration_page.fill_all_fields_correct_data()
            time.sleep(3)
