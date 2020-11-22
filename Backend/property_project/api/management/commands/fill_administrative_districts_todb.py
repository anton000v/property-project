from django.core.management.base import BaseCommand
from api.models import AdministrativeDistrict


class Command(BaseCommand):
    help = 'Fill in administrative districts to db'

    def handle(self, *args, **options):
        try:
            administrative_districts = [
                [['Шевченковский', 'Шевченківський'], []],
                [['Киевский', 'Київський'], []],
                [['Слободской', 'Слобідський'], ['Коминтерновский', 'Комінтернівський']],
                [['Основянский', "Основ'янський"], ['Червонозаводский', 'Червонозаводський']],
                [['Холодногорский', 'Холодногірський'], []],
                [['Московский', 'Московський'], []],
                [['Новобаварский', 'Новобаварський'], ['Октябрьский', 'Жовтневий']],
                [['Индустриальный', 'Індустріальний'], []],
                [['Немышлянский', 'Немишлянський'], ['Фрунзенский', 'Фрунзенський']],
            ]
            for dist in administrative_districts:
                record = AdministrativeDistrict()
                if (dist[1]):
                    record.administrative_old_dist_ru = dist[1][0]
                    record.administrative_old_dist_urk = dist[1][1]
                record.administrative_dist_ru = dist[0][0]
                record.administrative_dist_ukr = dist[0][1]
                record.save()
            print("Administrative districts are filled!")
        except Exception as e:
            print(str(e))