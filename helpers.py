import random
import string


def generate_login():
    number = random.randint(1000, 9999)
    login = f'test_testov_{number}@ya.ru'
    return login


def generate_password(length=6):
    alphabet = string.ascii_letters + string.digits
    password = ''
    for _ in range(length):
        password += random.choice(alphabet)
    return password
