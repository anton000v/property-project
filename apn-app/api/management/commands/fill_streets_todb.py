from django.core.management.base import BaseCommand
from utils.helpers import parse_streets
from api.models import Street


class Command(BaseCommand):
    help = 'Fill in streets to db'

    def handle(self, *args, **options):
        try:
            streets = parse_streets('api/static/txt/streets.txt')

            print("Try to filled streets...")
            for street in streets:
                record = Street()
                record.street_uk = street[0]
                record.street_ru = street[1]
                record.save()
            print("Streets are filled!")
        except Exception as e:
            print(str(e))