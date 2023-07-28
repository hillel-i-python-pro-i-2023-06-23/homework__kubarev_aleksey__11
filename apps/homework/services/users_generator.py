from faker import Faker
from typing import NamedTuple
from collections.abc import Iterator

faker = Faker()


class User(NamedTuple):
    username: str
    email: str


def generate_user() -> User:
    return User(
        username=faker.unique.first_name(),
        email=faker.unique.company_email(),
    )


def users_generator(amount: int) -> Iterator[User]:
    for index in range(1, amount + 1):
        yield generate_user()


def generate_list_of_users(amount: int = 100) -> list:
    users = users_generator(amount)
    list_of_users = []
    for user in users:
        username = user.username
        email = user.email
        list_of_users.append(f"<li><b>{username}</b> - <span>{email}</span></li>")
    return list_of_users


def output_info(users_dict: list) -> str:
    return "\n".join(users_dict)
