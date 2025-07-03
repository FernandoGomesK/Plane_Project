from faker import Faker
fake = Faker()
print(fake.name())

def new_func(fake):
    for i in range(10):
        print(fake.name())

new_func(fake)