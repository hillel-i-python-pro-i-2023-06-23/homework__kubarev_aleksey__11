import logging

from django.core.management.base import BaseCommand

from apps.animals.models import Animal
from apps.animals.services.generate_animals import generate_animals


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--amount",
            type=int,
            help="How many animals do you want to generate?",
            default=10,
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]

        # is_mark_as_autogenerated

        logger = logging.getLogger("django")

        queryset = Animal.objects.all()

        logger.info(f"Current amount of animals before: {queryset.count()}")

        for animal in generate_animals(amount=amount):
            animal.is_auto_generated = True
            animal.save()

        logger.info(f"Current amount of animals after: {queryset.count()}")