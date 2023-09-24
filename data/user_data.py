from faker import Faker


class User:
    first_name = Faker().first_name()
    last_name = Faker().last_name()
    email = Faker().email()
    telephone = Faker().phone_number()
    password = Faker().password()

