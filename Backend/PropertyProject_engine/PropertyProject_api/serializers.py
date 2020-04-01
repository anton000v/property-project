from rest_framework import serializers,fields
from . import choices
from . import fields
from .models import NewBuilding
from .models import Street

# class StreetField(serializers.StringRelatedField):
#     pass
    # def to_internal_value(self, value):
    #     return value

# class MicroDistrictSerializer(serializers.Serializer):
#     type = serializers.CharField(max_length=200)


# class JSONSerializerField(serializers.Field):
#     """ Serializer for JSONField -- required to make field writable"""
#     def to_internal_value(self, data):
#         return data
#     def to_representation(self, value):
#         return value
#
# class MySerializer(serializers.Serializer):
#     json = JSONSerializerField()
#
# class MicroDistrictSerializer(serializers.Serializer):
#     json = serializers.JSONField()

class NewBuildingSerializerForSearch(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    street = serializers.SlugRelatedField(slug_field="street_ru",queryset=Street.objects.all())
    house_number = serializers.CharField(max_length=10)
    house_letter = serializers.CharField(max_length=1)
    district = fields.ChoiceFieldCustomDisplay(choices=choices.DISTRICT_CHOICES,
                                default=choices.NOT_COMPLETED,
                                # source='get_district_display'
                                )  # )
    developer = serializers.CharField(max_length=100, default=1)  #
    slug = serializers.SlugField(max_length=150)

    

class NewBuildingSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    # messageG = forms.CharField(widget=forms.Textarea, label='lolkek')
    # address = models.CharField(max_length=200, verbose_name=u"Адрес", default=1)  # адресс
    # street = StreetField(read_only=False,queryset=Streets.objects.all())
    street = serializers.SlugRelatedField(slug_field="street_ru",queryset=Street.objects.all())
    house_number = serializers.CharField(max_length=10)
    house_letter = serializers.CharField(max_length=1)
    administrativeDistrict = fields.ChoiceFieldCustomDisplay(choices=choices.THE_ADMINISTRATIVE_DISTRICT_CHOICES,
                                              default=choices.NOT_COMPLETED,
                                              # source='get_administrativeDistrict_display',
                                              )  #
    district = fields.ChoiceFieldCustomDisplay(choices=choices.DISTRICT_CHOICES,
                                default=choices.NOT_COMPLETED,
                                # source='get_district_display'
                                )  # )
    micro_district = fields.ChoiceFieldCustomDisplay(choices=choices.FULL_MICRO_DISTRICT_CHOICES,
                                      default=choices.NOT_COMPLETED,
                                      # source='get_micro_district_display'
                                      )  # микрорайон
    location = serializers.CharField(max_length=200, default=1)  #
    developer = serializers.CharField(max_length=100, default=1)  #
    theClass = fields.ChoiceFieldCustomDisplay(choices=choices.THE_CLASS_CHOICES, default=choices.NOT_COMPLETED,
                                # source='get_theClass_display'
                                )
    numberOfStoreys = serializers.IntegerField(default=1)  #
    numberOfBuildings = serializers.IntegerField(default=1)  #
    numberOfSectionsOrEntrances = serializers.IntegerField(default=1)
    constructionTechnology = fields.ChoiceFieldCustomDisplay(choices=choices.THE_CONSTRUCTION_TECHNOLOGY_CHOICES,
                                              default=choices.NOT_COMPLETED,
                                              # source='get_constructionTechnology_display'
                                              )
    wallsType = fields.ChoiceFieldCustomDisplay(choices=choices.THE_WALLS_TYPE_CHOICES,  default=choices.NOT_COMPLETED,
                                # source='get_wallsType_display'
                                 )
    warming = fields.ChoiceFieldCustomDisplay(choices=choices.THE_WARMING_CHOICES, default=choices.NOT_COMPLETED,
                                # source='get_warming_display'
                               )  #
    roomHeight = serializers.IntegerField(default=1)  #
    numberOfApartmentsInTheHouse = serializers.IntegerField(default=1)  #

    # ----------------------------------------------------
    numberOfOneRoom = serializers.IntegerField(default=1)
    squareOfOneRoom = serializers.FloatField(default=1)
    numberOfTwoRoom = serializers.IntegerField(default=1)
    squareOfTwoRoom = serializers.FloatField(default=1)
    numberOfThreeRoom = serializers.IntegerField(default=1)
    squareOfThreeRoom = serializers.FloatField(default=1)
    numberOfFourRoom = serializers.IntegerField(default=1)
    squareOfFourRoom = serializers.FloatField(default=1)
    # ----------------------------------------------------

    numberOfApartmensPerFloor = serializers.IntegerField(default=1)  #
    commercialPremises = serializers.IntegerField(default=1)  # пишешь только этаж
    heating = fields.ChoiceFieldCustomDisplay(choices=choices.THE_HEATING_CHOICES, default=choices.NOT_COMPLETED,
                                # source='get_heating_display'
                              )
    gasification = serializers.BooleanField(default=1)
    elevator = serializers.CharField(max_length=50,default=1)  #
    parking = fields.ChoiceFieldCustomDisplay(choices=choices.THE_PARKING_CHOICES,default=choices.NOT_COMPLETED,)
                                # source='parking'
    parking = fields.MultipleChoiceFieldCustomDisplay(choices=choices.THE_PARKING_CHOICES,default=choices.NOT_COMPLETED)
    numberOfParkingSpaces = serializers.IntegerField(default=1)
    price = serializers.IntegerField(default=1)
    completionDate = serializers.IntegerField(default=1)
    description = serializers.CharField(default=1)

    slug = serializers.SlugField(max_length=150)
    lat = serializers.FloatField()
    lng = serializers.FloatField()
    #
    # def create(self, validated_data):
    #     print("VALIDATED DATA:  ",validated_data)
    #     return NewBuilding.objects.create(**validated_data)
