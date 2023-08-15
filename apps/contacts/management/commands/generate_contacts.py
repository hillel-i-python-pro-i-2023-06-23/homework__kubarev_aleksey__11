import logging

from django.core.management.base import BaseCommand

from apps.contacts.models import Contact
from apps.contacts.services.generate_contacts import generate_contacts


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--amount",
            type=int,
            help="How many contacts do you want to generate?",
            default=12,
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]

        logger = logging.getLogger("django")

        queryset = Contact.objects.all()

        logger.info(f"Current amount of contacts before: {queryset.count()}")

        for contact in generate_contacts(amount=amount):
            contact.save()

        logger.info(f"Current amount of contacts after: {queryset.count()}")
