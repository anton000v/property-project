import requests
from django.conf import settings


class House:
    key = settings.GOOGLE_PERSONAL_KEY

    def __init__(self, street, house_number, house_letter='', city='Харьков', country='Украина'):
        self.street = street
        self.house_number = house_number
        self.house_letter = house_letter
        self.house_district = ''
        self.city = city
        self.country = country
        self.lat = ''
        self.lng = ''
        self.address_components = ''
        self.google_geometry = ''

    def send_request(self, letter):
        url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {'address': '{} {} {} {}{}'.format(self.country, self.city, self.street, self.house_number, letter),
                  'key': settings.GOOGLE_PERSONAL_KEY, 'language': 'ru'}
        answer = requests.request(method='GET', url=url, params=params)
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
            for address_component in (results := json_answer['results'][0])['address_components']:
                if address_component['types'][0] == 'street_number':
                    if address_component['long_name'] == "{}{}".format(self.house_number, self.house_letter):
                        self.address_components = results['address_components']
                        self.google_geometry = results['geometry']
                        return True
                else:
                    continue
        print(f'{self.house_number}, {letter} does not exist')
        return False
