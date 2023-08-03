from collections.abc import Iterator

from faker import Faker

from apps.contacts.models import Contact

faker = Faker()


def generate_contact() -> Contact:
    return Contact(
        name=faker.first_name(),
        age=faker.pyint(min_value=1, max_value=47),
    )


def generate_contacts(amount: int) -> Iterator[Contact]:
    for _ in range(amount):
        yield generate_contact()
