from django.db import models

from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify
from django.utils.safestring import mark_safe
# from django.core.validators import MinValueValidator
# from decimal import Decimal

import PropertyProject_api.choices as choices

class Developer(models.Model):
    developer_name = models.CharField(max_length=150, verbose_name= "Название застройщика", unique=True)

    class Meta:
        verbose_name = 'Застройщик'
        verbose_name_plural = 'Застройщики'

    def __str__(self):
        return self.developer_name

class AdministrativeDistrict(models.Model):
    administrative_dist_ru = models.CharField(max_length=150)
    administrative_dist_ukr = models.CharField(max_length=150)
    administrative_old_dist_ru = models.CharField(max_length=150, null=True,blank=True)
    administrative_old_dist_urk = models.CharField(max_length=150, null=True,blank=True)

    def __str__(self):
        if self.administrative_old_dist_urk:
            return "{} - бывший {}".format(self.administrative_dist_ru, self.administrative_old_dist_ru)
        else:
            return "{}".format(self.administrative_dist_ru)

    class Meta:
        verbose_name = 'Административный район'
        verbose_name_plural = 'Административные районы'

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

    street = models.ForeignKey(Street,on_delete=models.CASCADE, verbose_name='Улица', related_name='street')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    house_letter = models.CharField(max_length=2, verbose_name='Буква дома',
                                    choices=choices.HOUSE_LETTER_CHOICES,
                                    null=True, blank=True,
                                    )

    administrative_district = models.ForeignKey(AdministrativeDistrict,on_delete=models.CASCADE, verbose_name="Административный район")
    # administrativeDistrict = models.CharField(max_length=2, choices=choices.THE_ADMINISTRATIVE_DISTRICT_CHOICES,
    #                                           default=choices.NOT_COMPLETED,
    #                                           verbose_name=u"Административный район")  #
    district = models.CharField(max_length=4, choices=choices.DISTRICT_CHOICES,
                                verbose_name=u"Район",
                                )  # )
    micro_district = models.CharField(max_length=4, choices=choices.FULL_MICRO_DISTRICT_CHOICES,
                                      default=choices.NOT_COMPLETED,
                                      verbose_name="Микрорайон",
                                      null=True, blank=True)  # микрорайон
    houising_number = models.CharField(max_length = 2, choices = choices.HOUSING_NUMBER_CHOICES,
                                      default=choices.NOT_DIVIDED,
                                      verbose_name='Номер корпуса',
                                      null=True, blank=True)

    location = models.CharField(max_length=200, verbose_name=u"Расположение", default=1, null=True, blank=True)  #
    # developer = models.CharField(max_length=100, verbose_name=u"Застройщик", default=1)  #
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, verbose_name = 'Застройщик', null=True, blank=True)
    the_class = models.CharField(max_length=2, choices=choices.THE_CLASS_CHOICES, default=choices.NOT_COMPLETED,
                                verbose_name=u"Класс", null=True, blank=True)
    number_of_storeys = models.PositiveSmallIntegerField(verbose_name=u"Этажность", default=1)  #
    number_of_buildings = models.PositiveSmallIntegerField(verbose_name=u"Количество домов", default=1)  #
    number_of_sections_or_entrances = models.IntegerField(verbose_name=u"Количество секций/подьездов",default=1)
    construction_technology = models.CharField(max_length=2, choices=choices.THE_CONSTRUCTION_TECHNOLOGY_CHOICES,
                                              default=choices.NOT_COMPLETED,
                                              verbose_name=u"Технология строительства", null=True, blank=True)
    walls_type = models.CharField(max_length=2, choices=choices.THE_WALLS_TYPE_CHOICES, default=choices.NOT_COMPLETED,
                                 verbose_name=u"Стены", null=True, blank=True)
    warming = models.CharField(max_length=2, choices=choices.THE_WARMING_CHOICES, default=choices.NOT_COMPLETED,
                               verbose_name=u"Утепление", null=True, blank=True)  #
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

    number_of_apartments_per_floor = models.PositiveSmallIntegerField(verbose_name=u"Кол-во квартир на этаже", default=1)
    commercial_premises = models.PositiveSmallIntegerField(verbose_name=u"Коммерческие помещения",
                                                          null=True, default=1)  # пишешь только этаж
    heating = models.CharField(max_length=2, choices=choices.THE_HEATING_CHOICES, default=choices.NOT_COMPLETED,
                               verbose_name=u"Отопление", null=True, blank=True)
    gasification = models.BooleanField(verbose_name=u"Газификация", default=1)
    elevator = models.CharField(max_length=50, verbose_name=u"Лифт", default=1)  #
    parking = MultiSelectField(choices=choices.THE_PARKING_CHOICES, default=choices.NOT_COMPLETED,
                               verbose_name=u"Паркинг", null=True, blank=True)
    number_of_parking_spaces = models.SmallIntegerField(verbose_name=u"Кол-во машиномест", default=1)
    price = models.SmallIntegerField(verbose_name=u"Цена за м2 у застройщика", default=1)
    completion_date = models.SmallIntegerField(verbose_name=u"Сдан и принят в эксплуатацию", default=1)
    description = models.TextField(verbose_name=u"Описание", default=1)

    slug = models.SlugField(max_length=150, unique=True, blank=True, )
    lat = models.FloatField(verbose_name='Широта', default=0, null=True, blank=True)
    lng = models.FloatField(verbose_name='Долгота', default=0, null=True, blank=True)


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
    building = models.ForeignKey(NewBuilding, on_delete=models.CASCADE, related_name='building_images', to_field='slug')
    building_image = models.ImageField(verbose_name='Фото', blank=True, null=True, editable=True)

    def __str__(self):
        return '%s - %s' % (self.building, self.building_image)

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.building_image.url))

    image_tag.short_description = 'Image'

    # def url(self):
    #     # returns a URL for either internal stored or external image url
    #     if self.externalURL:
    #         return self.externalURL
    #     else:
    #         # is this the best way to do this??
    #         return os.path.join('/',settings.MEDIA_URL, os.path.basename(str(self.building_image)))

    # def image_tag(self):
    #     # used in the admin site model as a "thumbnail"
    #     return mark_safe('<img src="{}" width="150" height="150" />'.format(self.building_image) )
    # image_tag.short_description = 'Image'
    # def image_tag(self):
    #     return '<img src="{}" />'.format(building_image)
    # image_tag.short_description = 'Изображение'
    # image_tag.allow_tags = True

class LayoutImage(models.Model):
    building = models.ForeignKey(NewBuilding, on_delete=models.CASCADE, related_name='layout_images', to_field='slug')
    layout_image = models.ImageField(verbose_name='Планировки', blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.building, self.layout_image)

    # def image_tag(self):
    #     return '<img src="{}" />'.format(layout_image)
    # image_tag.short_description = 'Планировка'
    # image_tag.allow_tags = True

class WayFromMetro(models.Model):
    building = models.ForeignKey(NewBuilding, on_delete=models.CASCADE, related_name='ways_from_metro', to_field='slug')
    metro = models.CharField(max_length=3, choices=choices.THE_METRO_CHOICES, default=choices.NOT_COMPLETED,
                                    verbose_name=u"Метро")
    time = models.SmallIntegerField(verbose_name=u"Время", default=1)
    type_of_movement = models.CharField(max_length=2, choices=choices.THE_TYPE_OF_MOVEMENT_CHOICES,
                                      default=choices.NOT_COMPLETED,
                                      verbose_name=u"Как")
    number_of_meters = models.SmallIntegerField(verbose_name=u"Расстояние", default=1)

    def __str__(self):
        return '%s - %s' % (self.building, self.metro)
