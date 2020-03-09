from rest_framework import serializers,fields
from . import choices
class NewBuildingSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    # messageG = forms.CharField(widget=forms.Textarea, label='lolkek')
    # address = models.CharField(max_length=200, verbose_name=u"Адрес", default=1)  # адресс
    street = serializers.StringRelatedField()
    house_number = serializers.CharField(max_length=10)
    house_letter = serializers.CharField(max_length=1)
    administrativeDistrict = serializers.ChoiceField(choices=choices.THE_ADMINISTRATIVE_DISTRICT_CHOICES,
                                              default=choices.NOT_COMPLETED, source='get_administrativeDistrict_display',
                                              )  #
    district = serializers.ChoiceField(choices=choices.DISTRICT_CHOICES,
                                default=choices.NOT_COMPLETED,
                                source='get_district_display'
                                )  # )
    micro_district = serializers.ChoiceField(choices=choices.FULL_MICRO_DISTRICT_CHOICES,
                                      default=choices.NOT_COMPLETED,
                                      source='get_micro_district_display'
                                      )  # микрорайон
    location = serializers.CharField(max_length=200, default=1)  #
    developer = serializers.CharField(max_length=100, default=1)  #
    theClass = serializers.ChoiceField(choices=choices.THE_CLASS_CHOICES, default=choices.NOT_COMPLETED,
                                source='get_theClass_display')
    numberOfStoreys = serializers.IntegerField(default=1)  #
    numberOfBuildings = serializers.IntegerField(default=1)  #
    numberOfSectionsOrEntrances = serializers.CharField(max_length=100,
                                                   default=1)
    constructionTechnology = serializers.ChoiceField(choices=choices.THE_CONSTRUCTION_TECHNOLOGY_CHOICES,
                                              default=choices.NOT_COMPLETED,
                                              source='get_constructionTechnology_display'
                                              )
    wallsType = serializers.ChoiceField(choices=choices.THE_WALLS_TYPE_CHOICES,  default=choices.NOT_COMPLETED,
                                source='get_wallsType_display'
                                 )
    warming = serializers.ChoiceField(choices=choices.THE_WARMING_CHOICES, default=choices.NOT_COMPLETED,
                                source='get_warming_display'
                               )  #
    roomHeight = serializers.IntegerField(default=1)  #
    numberOfApartmentsInTheHouse = serializers.IntegerField(default=1)  #

    # ----------------------------------------------------
    numberOfOneRoom = serializers.IntegerField(default=1)
    squareOfOneRoom = serializers.IntegerField(default=1)
    numberOfTwoRoom = serializers.IntegerField(default=1)
    squareOfTwoRoom = serializers.IntegerField(default=1)
    numberOfThreeRoom = serializers.IntegerField(default=1)
    squareOfThreeRoom = serializers.IntegerField(default=1)
    numberOfFourRoom = serializers.IntegerField(default=1)
    squareOfFourRoom = serializers.IntegerField(default=1)
    # ----------------------------------------------------

    numberOfApartmensPerFloor = serializers.IntegerField(default=1)  #
    commercialPremises = serializers.IntegerField(default=1)  # пишешь только этаж
    heating = serializers.ChoiceField(choices=choices.THE_HEATING_CHOICES, default=choices.NOT_COMPLETED,
                                source='get_heating_display'
                              )
    gasification = serializers.BooleanField(default=1)
    elevator = serializers.CharField(max_length=50,default=1)  #
    parking = fields.MultipleChoiceField(choices=choices.THE_PARKING_CHOICES,default=choices.NOT_COMPLETED,
                                source='get_parking_display'
                              )
    numberOfParkingSpaces = serializers.IntegerField(default=1)
    price = serializers.IntegerField(default=1)
    completionDate = serializers.IntegerField(default=1)
    description = serializers.CharField(default=1)

    slug = serializers.SlugField(max_length=150, read_only=True)
