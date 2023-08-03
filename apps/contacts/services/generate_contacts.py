from collections.abc import Iterator
from faker import Faker
from apps.contacts.models import Contact

faker = Faker()


def generate_phone_number() -> str:
    country_code = "380"
    region_code = faker.random_int(10, 99)  # Generate a two-digit region code
    subscriber_number = faker.random_int(1000000, 9999999)  # Generate a seven-digit subscriber number
    phone_number = f"{country_code}{region_code:02d}{subscriber_number:07d}"
    return phone_number


def generate_contact() -> Contact:
    return Contact(
        name=faker.first_name(),
        phone_number=generate_phone_number(),
    )


def generate_contacts(amount: int) -> Iterator[Contact]:
    for _ in range(amount):
        yield generate_contact()
