from data.data import *
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()
def generated_person():
    yield Person(
        user_name=faker_en.first_name(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        password=faker_en.email(),
    )