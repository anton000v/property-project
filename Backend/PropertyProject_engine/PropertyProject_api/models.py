from django.db import models

from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify
# from django.core.validators import MinValueValidator
# from decimal import Decimal

import PropertyProject_api.choices as choices

class District(models.Model):
    dist_ru = models.CharField(max_length=150)
    dist_ukr = models.CharField(max_length=150)
    old_dist_ru = models.CharField(max_length=150, null=True,blank=True)
    old_dist_urk = models.CharField(max_length=150, null=True,blank=True)

    def __str__(self):
        return "{} - {}".format(self.dist_ru,self.dist_ukr)

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

class Street(models.Model):
    street_ru = models.CharField(max_length=150, verbose_name="Улица на русском")
    street_uk = models.CharField(max_length=150, verbose_name="Улица на украинском")

    def __str__(self):
        return self.street_ru

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'

class NewBuilding(models.Model):
    # class Meta():
    #     db_table = 'Новострои'
        # ordering = ['name']

    name = models.CharField(max_length=200, verbose_name=u'Название', default=1)

    street = models.ForeignKey(Street,on_delete=models.CASCADE, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    house_letter = models.CharField(max_length=2, verbose_name='Буква дома',
                                    choices=choices.HOUSE_LETTER_CHOICES,
                                    null=True, blank=True,
                                    )

    administrative_district = models.ForeignKey(District,on_delete=models.CASCADE, verbose_name="Административный район")
    # administrativeDistrict = models.CharField(max_length=2, choices=choices.THE_ADMINISTRATIVE_DISTRICT_CHOICES,
    #                                           default=choices.NOT_COMPLETED,
    #                                           verbose_name=u"Административный район")  #
    district = models.CharField(max_length=4, choices=choices.DISTRICT_CHOICES,
                                default=choices.NOT_COMPLETED,
                                verbose_name=u"Район")  # )
    micro_district = models.CharField(max_length=4, choices=choices.FULL_MICRO_DISTRICT_CHOICES,
                                      default=choices.NOT_COMPLETED,
                                      verbose_name="Микрорайон")  # микрорайон
    houising_number = models.CharField(max_length = 1, choices = choices.HOUSING_NUMBER_CHOICES,
                                      default=choices.NOT_DIVIDED,
                                      verbose_name='Номер корпуса',
                                      null=True, blank=True)

    location = models.CharField(max_length=200, verbose_name=u"Расположение", default=1)  #
    developer = models.CharField(max_length=100, verbose_name=u"Застройщик", default=1)  #
    the_class = models.CharField(max_length=2, choices=choices.THE_CLASS_CHOICES, default=choices.NOT_COMPLETED,
                                verbose_name=u"Класс")
    number_of_storeys = models.PositiveSmallIntegerField(verbose_name=u"Этажность", default=1)  #
    number_of_buildings = models.PositiveSmallIntegerField(verbose_name=u"Количество домов", default=1)  #
    number_of_sections_or_entrances = models.IntegerField(verbose_name=u"Количество секций/подьездов",default=1)
    construction_technology = models.CharField(max_length=2, choices=choices.THE_CONSTRUCTION_TECHNOLOGY_CHOICES,
                                              default=choices.NOT_COMPLETED,
                                              verbose_name=u"Технология строительства")
    walls_type = models.CharField(max_length=2, choices=choices.THE_WALLS_TYPE_CHOICES, default=choices.NOT_COMPLETED,
                                 verbose_name=u"Стены")
    warming = models.CharField(max_length=2, choices=choices.THE_WARMING_CHOICES, default=choices.NOT_COMPLETED,
                               verbose_name=u"Утепление")  #
    room_height = models.PositiveSmallIntegerField(verbose_name=u"Высота помещений", default=1)  #
    number_of_apartments_in_house = models.PositiveSmallIntegerField(verbose_name=u"Кол-во квартир в доме", default=1)  #

    # ----------------------------------------------------
    number_of_one_room = models.PositiveSmallIntegerField(verbose_name=u"Кол-во 1к.кв.", default=1)
    square_of_one_room = models.FloatField(verbose_name=u"Площадь 1к.кв.", default=1)
    number_of_two_room = models.PositiveSmallIntegerField(verbose_name=u"Кол-во 2к.кв.", default=1)
    square_of_two_room = models.FloatField(verbose_name=u"Площадь 2к.кв.", default=1)
    number_of_three_room = models.PositiveSmallIntegerField(verbose_name=u"Кол-во 3к.кв.", default=1)
    square_of_three_room = models.FloatField(verbose_name=u"Площадь 3к.кв.", default=1)
    number_of_four_room = models.PositiveSmallIntegerField(verbose_name=u"Кол-во 4к.кв.", default=1)
    square_of_four_room = models.FloatField(verbose_name=u"Площадь 4к.кв.", default=1)
    # ----------------------------------------------------

    number_of_apartments_per_floor = models.PositiveSmallIntegerField(verbose_name=u"Кол-во квартир на этаже", default=1)  #
    commercial_premises = models.PositiveSmallIntegerField(verbose_name=u"Коммерческие помещения",
                                                          null=True, default=1)  # пишешь только этаж
    heating = models.CharField(max_length=2, choices=choices.THE_HEATING_CHOICES, default=choices.NOT_COMPLETED,
                               verbose_name=u"Отопление")
    gasification = models.BooleanField(verbose_name=u"Газификация", default=1)
    elevator = models.CharField(max_length=50, verbose_name=u"Лифт", default=1)  #
    parking = MultiSelectField(choices=choices.THE_PARKING_CHOICES, default=choices.NOT_COMPLETED,
                               verbose_name=u"Паркинг")
    number_of_parking_spaces = models.SmallIntegerField(verbose_name=u"Кол-во машиномест", default=1)
    price = models.SmallIntegerField(verbose_name=u"Цена за м2 у застройщика", default=1)
    completion_date = models.SmallIntegerField(verbose_name=u"Сдан и принят в эксплуатацию", default=1)
    description = models.TextField(verbose_name=u"Описание", default=1)

    slug = models.SlugField(max_length=150, unique=True, blank=True, )  # editable = False
    lat = models.FloatField(verbose_name='Широта', default=0)
    lng = models.FloatField(verbose_name='Долгота', default=0)


    # SEE HOW DOES IT WORK WITH VUEJS
    def get_absolute_url(self):
        return reverse('property_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('property_edit', kwargs={'slug': self.slug})


    def __str__(self):
        return self.slug


    class Meta:
        verbose_name = 'Новострой'
        verbose_name_plural = 'Новострои'


class BuildingImage(models.Model):
    building = models.ForeignKey(NewBuilding, on_delete=models.CASCADE, related_name='buildingImages')
    buildingImage = models.ImageField(verbose_name='Фото', blank=True, null=True, editable=True)

    def __str__(self):
        return '%s - %s' % (self.building, self.buildingImage)


class LayoutImage(models.Model):
    building = models.ForeignKey(NewBuilding, on_delete=models.CASCADE, related_name='layoutImages')
    layoutImage = models.ImageField(verbose_name='Планировки', blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.building, self.layoutImage)


class WayFromMetro(models.Model):
    building = models.ForeignKey(NewBuilding, on_delete=models.CASCADE, related_name='wayFromMetro', )
    metroChoices = models.CharField(max_length=3, choices=choices.THE_METRO_CHOICES, default=choices.NOT_COMPLETED,
                                    verbose_name=u"Метро")
    time = models.SmallIntegerField(verbose_name=u"Время", default=1)
    typeOfMovement = models.CharField(max_length=2, choices=choices.THE_TYPE_OF_MOVEMENT_CHOICES,
                                      default=choices.NOT_COMPLETED,
                                      verbose_name=u"Как")
    numberOfMeters = models.SmallIntegerField(verbose_name=u"Расстояние", default=1)

    def __str__(self):
        return '%s - %s' % (self.building, self.metroChoices)
