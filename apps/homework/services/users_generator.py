from faker import Faker
from typing import NamedTuple
from collections.abc import Iterator

faker = Faker()


class User(NamedTuple):
    username: str
    email: str
    password: str


def generate_user(used_usernames: set, used_emails: set, used_passwords: set) -> User:
    while True:
        username = faker.unique.first_name()
        email = faker.unique.company_email()
        password = faker.password()

        if username not in used_usernames and email not in used_emails and password not in used_passwords:
            used_usernames.add(username)
            used_emails.add(email)
            used_passwords.add(password)
            return User(username=username, email=email, password=password)


def users_generator(amount: int) -> Iterator[User]:
    used_usernames = set()
    used_emails = set()
    used_passwords = set()

    for index in range(1, amount + 1):
        yield generate_user(used_usernames, used_emails, used_passwords)


def generate_list_of_users(amount: int = 100) -> list:
    users = users_generator(amount)
    list_of_users = []
    for user in users:
        username = user.username
        email = user.email
        password = user.password
        list_of_users.append(f"<li><b>{username}</b> - <span>{email}</span> - <i>{password}</i></li>")
    return list_of_users


def output_info(users_list: list) -> str:
    return "\n".join(users_list)
