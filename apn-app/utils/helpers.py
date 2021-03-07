from itertools import product
from pytils.translit import slugify
from api import models


def generate_slug(address):
    return slugify(address)


# def fill_administrative_districts_todb():
#     administrative_districts = [
#         [['Шевченковский', 'Шевченківський'], []],
#         [['Киевский', 'Київський'], []],
#         [['Слободской', 'Слобідський'], ['Коминтерновский', 'Комінтернівський']],
#         [['Основянский', "Основ'янський"], ['Червонозаводский', 'Червонозаводський']],
#         [['Холодногорский', 'Холодногірський'], []],
#         [['Московский', 'Московський'], []],
#         [['Новобаварский', 'Новобаварський'], ['Октябрьский', 'Жовтневий']],
#         [['Индустриальный', 'Індустріальний'], []],
#         [['Немышлянский', 'Немишлянський'], ['Фрунзенский', 'Фрунзенський']],
#     ]
#     for dist in administrative_districts:
#         record = models.AdministrativeDistrict()
#         if (dist[1]):
#             record.administrative_old_dist_ru = dist[1][0]
#             record.administrative_old_dist_urk = dist[1][1]
#         record.administrative_dist_ru = dist[0][0]
#         record.administrative_dist_ukr = dist[0][1]
#         record.save()
#     print("Administrative districts are filled!")


def parse_streets(path):
    streets = []
    print("Try to parse streets...")
    for line in open(path, 'r'):
        data = [dataItem.strip() for dataItem in line.strip().split(' | ')]
        streets.append(data)
    print("Streets are parsed")
    streets.sort(key=lambda x: x[1])
    return streets


# def fill_streets_todb():
#     streets = parse_streets('api/static/txt/streets.txt')
#
#     print("Try to filled streets...")
#     for street in streets:
#         record = models.Street()
#         record.street_uk = street[0]
#         record.street_ru = street[1]
#         record.save()
#     print("Streets are filled!")


def cartesian_product_dict(**kwargs):
    keys = kwargs.keys()
    vals = kwargs.values()

    for instance in product(*vals):
        yield dict(zip(keys, instance))