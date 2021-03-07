from rest_framework import serializers
from api import choices, fields, models, choices, fields


class ExtraFieldsMixin:
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return self.Meta.extra_fields + expanded_fields
        else:
            return expanded_fields


# class StreetSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = models.Street
# 		fields = '__all__'

# class AdministrativeDistrictSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = models.AdministrativeDistrict
# 		fields = '__all__'

# class DeveloperSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = models.Developer
# 		fields = '__all__'

class WayFromMetroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WayFromMetro
        fields = '__all__'


class BuildingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BuildingImage
        fields = '__all__'


class LayoutImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LayoutImage
        fields = '__all__'


class NewBuildingSerializer(serializers.ModelSerializer, ExtraFieldsMixin):
    street = serializers.SlugRelatedField(slug_field="street_ru", queryset=models.Street.objects.all())
    administrative_district = serializers.SlugRelatedField(slug_field="administrative_dist_ru",
                                                           queryset=models.AdministrativeDistrict.objects.all())
    developer = serializers.SlugRelatedField(slug_field="developer_name", queryset=models.Developer.objects.all())
    ways_from_metro = WayFromMetroSerializer(many=True)
    building_images = BuildingImageSerializer(many=True)
    layout_images = LayoutImageSerializer(many=True)
    district = fields.ChoiceFieldCustomDisplay(choices=choices.DISTRICT_CHOICES, default=choices.NOT_COMPLETED)
    micro_district = fields.ChoiceFieldCustomDisplay(choices=choices.FULL_MICRO_DISTRICT_CHOICES,
                                                     default=choices.NOT_COMPLETED)
    construction_technology = fields.ChoiceFieldCustomDisplay(choices=choices.THE_CONSTRUCTION_TECHNOLOGY_CHOICES,
                                                              default=choices.NOT_COMPLETED)
    heating = fields.ChoiceFieldCustomDisplay(choices=choices.THE_HEATING_CHOICES, default=choices.NOT_COMPLETED)
    parking = fields.MultipleChoiceFieldCustomDisplay(choices=choices.THE_PARKING_CHOICES,
                                                      default=choices.NOT_COMPLETED)
    the_class = fields.ChoiceFieldCustomDisplay(choices=choices.THE_CLASS_CHOICES, default=choices.NOT_COMPLETED)

    class Meta:
        model = models.NewBuilding
        fields = '__all__'
        extra_fields = ['parking', 'district', 'micro_district', 'street', 'construction_technology', 'heating',
                        'the_class', 'construction_technology', 'administrative_district', 'developer',
                        'ways_from_metro', 'building_images', 'layout_images']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

# class BuildingImageSerializer(serializers.Serializer):
#     building_image = serializers.ImageField()


# class LayoutImageSerializer(serializers.Serializer):
#     layout_image = serializers.ImageField()


# class WayFromMetroSerializer(serializers.Serializer):
#     metro_choices = fields.ChoiceFieldCustomDisplay(choices=choices.THE_METRO_CHOICES,
#                                                     default=choices.NOT_COMPLETED,
#                                               # source='get_administrativeDistrict_display',
#                                               )  #
#     time = serializers.IntegerField(default=1)
#     type_of_movement = fields.ChoiceFieldCustomDisplay(choices=choices.THE_TYPE_OF_MOVEMENT_CHOICES,
#                                                     default=choices.NOT_COMPLETED,
#                                               # source='get_administrativeDistrict_display',
#                                               )  #
#     number_of_meters = serializers.IntegerField(default=1)

# class NewBuildingSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=200)
#     # messageG = forms.CharField(widget=forms.Textarea, label='lolkek')
#     # address = models.CharField(max_length=200, verbose_name=u"Адрес", default=1)  # адресс
#     # street = StreetField(read_only=False,queryset=Streets.objects.all())
#     street = serializers.SlugRelatedField(slug_field="street_ru",queryset=Street.objects.all())
#     house_number = serializers.CharField(max_length=10)
#     house_letter = serializers.CharField(max_length=1)
#     administrative_district = serializers.SlugRelatedField(slug_field="administrative_dist_ru",queryset=AdministrativeDistrict.objects.all()) # ВОЗМОЖНЫ ОШИБКИ СЕРИАЛИЗАЦИИ из-за разницы в именах модели и админ района сериализатора!!!!!!!!!!
#     district = fields.ChoiceFieldCustomDisplay(choices=choices.DISTRICT_CHOICES,
#                                 default=choices.NOT_COMPLETED,
#                                 # source='get_district_display'
#                                 )  # )
#     micro_district = fields.ChoiceFieldCustomDisplay(choices=choices.FULL_MICRO_DISTRICT_CHOICES,
#                                       default=choices.NOT_COMPLETED,
#                                       # source='get_micro_district_display'
#                                       )  # микрорайон
#     location = serializers.CharField(max_length=200, default=1)  #
#     developer = serializers.SlugRelatedField(slug_field="developer_name",queryset=Developer.objects.all()) 
#     # developer = serializers.CharField(max_length=100, default=1)  #
#     theClass = fields.ChoiceFieldCustomDisplay(choices=choices.THE_CLASS_CHOICES, default=choices.NOT_COMPLETED,
#                                 # source='get_theClass_display'
#                                 )
#     numberOfStoreys = serializers.IntegerField(default=1)  #
#     numberOfBuildings = serializers.IntegerField(default=1)  #
#     numberOfSectionsOrEntrances = serializers.IntegerField(default=1)
#     constructionTechnology = fields.ChoiceFieldCustomDisplay(choices=choices.THE_CONSTRUCTION_TECHNOLOGY_CHOICES,
#                                               default=choices.NOT_COMPLETED,
#                                               # source='get_constructionTechnology_display'
#                                               )
#     wallsType = fields.ChoiceFieldCustomDisplay(choices=choices.THE_WALLS_TYPE_CHOICES,  default=choices.NOT_COMPLETED,
#                                 # source='get_wallsType_display'
#                                  )
#     warming = fields.ChoiceFieldCustomDisplay(choices=choices.THE_WARMING_CHOICES, default=choices.NOT_COMPLETED,
#                                 # source='get_warming_display'
#                                )  #
#     roomHeight = serializers.IntegerField(default=1)  #
#     numberOfApartmentsInTheHouse = serializers.IntegerField(default=1)  #

#     # ----------------------------------------------------
#     numberOfOneRoom = serializers.IntegerField(default=1)
#     squareOfOneRoom = serializers.FloatField(default=1)
#     numberOfTwoRoom = serializers.IntegerField(default=1)
#     squareOfTwoRoom = serializers.FloatField(default=1)
#     numberOfThreeRoom = serializers.IntegerField(default=1)
#     squareOfThreeRoom = serializers.FloatField(default=1)
#     numberOfFourRoom = serializers.IntegerField(default=1)
#     squareOfFourRoom = serializers.FloatField(default=1)
#     # ----------------------------------------------------

#     numberOfApartmensPerFloor = serializers.IntegerField(default=1)  #
#     commercialPremises = serializers.IntegerField(default=1)  # пишешь только этаж
#     heating = fields.ChoiceFieldCustomDisplay(choices=choices.THE_HEATING_CHOICES, default=choices.NOT_COMPLETED,
#                                 # source='get_heating_display'
#                               )
#     gasification = serializers.BooleanField(default=1)
#     elevator = serializers.CharField(max_length=50,default=1)  #
#     parking = fields.ChoiceFieldCustomDisplay(choices=choices.THE_PARKING_CHOICES,default=choices.NOT_COMPLETED,)
#                                 # source='parking'
#     parking = fields.MultipleChoiceFieldCustomDisplay(choices=choices.THE_PARKING_CHOICES,default=choices.NOT_COMPLETED)
#     numberOfParkingSpaces = serializers.IntegerField(default=1)
#     price = serializers.IntegerField(default=1)
#     completionDate = serializers.IntegerField(default=1)
#     description = serializers.CharField(default=1)

#     slug = serializers.SlugField(max_length=150)
#     lat = serializers.FloatField()
#     lng = serializers.FloatField()

#     building_images = BuildingImageSerializer(many=True)
#     layout_images = LayoutImageSerializer(many=True)
#     ways_from_metro = WayFromMetroSerializer(many=True)
