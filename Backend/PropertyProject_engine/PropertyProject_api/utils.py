from . import models
from local_settings import GOOGLE_PERSONAL_KEY
# from django.utils.text import slugify
from pytils.translit import slugify
from itertools import product
import requests

rus_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def generate_slug(address):
    return slugify(address)

def fill_administrative_districts_todb():
    administrative_districts = [
    [['Шевченковский', 'Шевченківський'],[]],
    [['Киевский', 'Київський'],[]],
    [['Слободской', 'Слобідський'],['Коминтерновский','Комінтернівський']],
    [['Основянский', "Основ'янський"],['Червонозаводский','Червонозаводський']],
    [['Холодногорский', 'Холодногірський'],[]],
    [['Московский', 'Московський'],[]],
    [['Новобаварский', 'Новобаварський'],['Октябрьский','Жовтневий']],
    [['Индустриальный', 'Індустріальний'],[]],
    [['Немышлянский', 'Немишлянський'],['Фрунзенский','Фрунзенський']],
    ]
    for dist in administrative_districts:
        record = models.AdministrativeDistrict()
        if(dist[1]):
            record.administrative_old_dist_ru = dist[1][0]
            record.administrative_old_dist_urk = dist[1][1]
        record.administrative_dist_ru = dist[0][0]
        record.administrative_dist_ukr = dist[0][1]
        record.save()
    print("Administrative districts are filled!")

def parse_streets(path):
    streets = []
    print("Try to parse streets...")
    for line in open(path,'r'):
        data = [dataItem.strip() for  dataItem in line.strip().split(' | ')]
        streets.append(data)
    print("Streets are parsed")
    streets.sort(key=lambda x:x[1])
    return streets

def fill_streets_todb():
    streets = parse_streets('PropertyProject_api/static/txt/streets.txt')

    print("Try to filled streets...")
    for street in streets:
        record = models.Street()
        record.street_uk = street[0]
        record.street_ru = street[1]
        record.save()
    print("Streets are filled!")

def cartesian_product_dict(**kwargs):
    keys = kwargs.keys()
    vals = kwargs.values()
    
    # print(vals)
    for instance in product(*vals):
        yield dict(zip(keys, instance))

class House():
    key = GOOGLE_PERSONAL_KEY
    def __init__(self,street, house_number, house_letter='', city='Харьков',country='Украина'):
        self.street = street
        self.house_number = house_number
        self.house_letter = house_letter
        self.house_district = ''
        self.city = city
        self.country = country
        self.lat = ''
        self.lng = ''
        self.address_components = ''
        self.google_geometry= ''


    def send_request(self, letter):
        url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {'address': '{} {} {} {}{}'.format(self.country,self.city,self.street,self.house_number,letter),'key':GOOGLE_PERSONAL_KEY,'language':'ru'}
        answer = requests.request(method='GET',url=url,params=params)
        return answer


    def fill_district(self):
        for d in self.address_components:
            if 'sublocality_level_1' in d['types']:
                self.house_district = d['long_name']


    def fill_location(self):
        lat_lng_dict = self.google_geometry['location']
        self.lat = lat_lng_dict['lat']
        self.lng = lat_lng_dict['lng']


    def is_exist(self, with_letter=True):
        if with_letter:
            letter = self.house_letter
        else:
            letter = ''
        json_answer = self.send_request(self.house_letter).json()
        if json_answer['status'] == 'OK':
            for address_component in (results:=json_answer['results'][0])['address_components']:
                if address_component['types'][0] == 'street_number':
                    if address_component['long_name'] == "{}{}".format(self.house_number,self.house_letter):
                        self.address_components = results['address_components']
                        self.google_geometry = results['geometry']
                        return True
                else:
                    continue
        print("{}{}".format(self.house_number,letter), ' does not exist')
        return False
