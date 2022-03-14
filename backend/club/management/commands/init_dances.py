import json

from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError

from club.models import Dance


class Command(BaseCommand):
    help = 'Inits dances for app'

    def handle(self, *args, **options):
        with open('resources/dances.json') as f:
            data = json.load(f)
            for item in data:
                try:
                    dance = Dance.objects.create(**item)
                    self.stdout.write(self.style.SUCCESS(f'Successfully added {dance.style}'))
                except IntegrityError:
                    self.stdout.write(self.style.ERROR(f'{item["style"]} has already exits'))
