from django.test import TestCase

from api import choices
from api import models


class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        
        models.Street.objects.create(
            street_ru = '1 улица на русском',
            street_uk = '1 вулиця на українському',
        )
        models.AdministrativeDistrict.objects.create(
            administrative_dist_ru = 'Административный район на русском',
            administrative_dist_ukr = 'Адміністративний район російською',
            administrative_old_dist_ru = 'Старый административный район на русском',
            administrative_old_dist_urk = 'Старий адміністративний район російською',
        )

        models.NewBuilding.objects.create(
            name='Test name', 
            street=models.Street.objects.all()[0],
            house_number=10,
            house_letter='д',
            administrative_district=models.AdministrativeDistrict.objects.all()[0],
            district=choices.SALTOVKA,
            micro_district=choices.m601,
            houising_number=choices.NOT_DIVIDED,
            location = 'test location',
            developer = 'test developer',
            the_class = choices.NOT_COMPLETED,
            number_of_storeys = 10,
            number_of_buildings = 1,
            number_of_sections_or_entrances = 2,
            construction_technology = choices.NOT_COMPLETED,
            walls_type = choices.NOT_COMPLETED,
            warming = choices.NOT_COMPLETED,
            room_height = 3,
            number_of_apartments_in_house = 90,
            number_of_one_room = 10,
            square_of_one_room = 2,
            number_of_two_room= 10,
            square_of_two_room = 2,
            number_of_three_room= 10,
            square_of_three_room = 2,
            number_of_four_room= 10,
            square_of_four_room = 2,
            number_of_apartments_per_floor = 2,
            commercial_premises = 2,
            heating = choices.NOT_COMPLETED,
            gasification = 1,
            elevator = 'yes',
            parking = choices.NOT_COMPLETED,
            number_of_parking_spaces =2 ,
            price = 2,
            completion_date = 1,
            description = 'some description',
            slug = '',
            lat = '100',
            lng = '200',
            )



    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_not_completed(self):
        building = models.NewBuilding.objects.get(id=1)
        nc = building.parking[0]
        self.assertEquals(nc,choices.NOT_COMPLETED)

    def test_old_administrative_district(self):
        admin_dist = models.AdministrativeDistrict.objects.all()[0]
        old_val = admin_dist.administrative_old_dist_ru
        self.assertEquals(old_val,'Старый административный район на русском')
    # def test_slug(self):
    #     building = models.NewBuilding.objects.get(id=1)
    #     slug = building.slug
    #     print('Test slug:',slug)
    #     self.assertEquals(slug,'1-ulitsa-na-russcom-10-d')


