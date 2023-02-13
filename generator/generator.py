from data.data import *
from faker import Faker
import random

faker_ru = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()
def generated_person():
    yield Person(
        username=faker_en.user_name(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        password=faker_en.password(length=(random.randint(8, 30))),
        double_last_name=faker_en.last_name()+'-'+faker_en.last_name(),
        double_first_name=faker_en.first_name()+'-'+faker_en.first_name(),
    )