# from rest_framework import serializers,fields
# from . import choices
# from . import fields
# # from .models import NewBuilding, BuildingImage, WayFromMetro
# from .models import Street, AdministrativeDistrict, Developer


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


# class NewBuildingSerializerForSearch(serializers.Serializer):
#     name = serializers.CharField(max_length=200)
#     street = serializers.SlugRelatedField(slug_field="street_ru",queryset=Street.objects.all())
#     administrative_district = serializers.SlugRelatedField(slug_field="administrative_dist_ru",queryset=AdministrativeDistrict.objects.all())
#     house_number = serializers.CharField(max_length=10)
#     house_letter = serializers.CharField(max_length=1)
#     district = fields.ChoiceFieldCustomDisplay(choices=choices.DISTRICT_CHOICES,
#                                 default=choices.NOT_COMPLETED,
#                                 # source='get_district_display'
#                                 )  # )
#     developer = serializers.CharField(max_length=100, default=1)
#     slug = serializers.SlugField(max_length=150)
#     building_images = BuildingImageSerializer(many=True)
#     layout_images = LayoutImageSerializer(many=True)
#     ways_from_metro = WayFromMetroSerializer(many=True)

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
#     the_class = fields.ChoiceFieldCustomDisplay(choices=choices.THE_CLASS_CHOICES, default=choices.NOT_COMPLETED,
#                                 # source='get_theClass_display'
#                                 )
#     number_of_storeys = serializers.IntegerField(default=1)  #
#     number_of_buildings = serializers.IntegerField(default=1)  #
#     number_of_sections_or_entrances = serializers.IntegerField(default=1)
#     construction_technology = fields.ChoiceFieldCustomDisplay(choices=choices.THE_CONSTRUCTION_TECHNOLOGY_CHOICES,
#                                               default=choices.NOT_COMPLETED,
#                                               # source='get_constructionTechnology_display'
#                                               )
#     walls_type = fields.ChoiceFieldCustomDisplay(choices=choices.THE_WALLS_TYPE_CHOICES,  default=choices.NOT_COMPLETED,
#                                 # source='get_wallsType_display'
#                                  )
#     warming = fields.ChoiceFieldCustomDisplay(choices=choices.THE_WARMING_CHOICES, default=choices.NOT_COMPLETED,
#                                 # source='get_warming_display'
#                                )  #
#     room_height = serializers.IntegerField(default=1)  #
#     number_of_apartments_in_the_house = serializers.IntegerField(default=1)  #

#     # ----------------------------------------------------
#     number_of_one_room = serializers.IntegerField(default=1)
#     square_of_one_room = serializers.FloatField(default=1)
#     number_of_two_room = serializers.IntegerField(default=1)
#     square_of_two_room = serializers.FloatField(default=1)
#     number_of_three_room = serializers.IntegerField(default=1)
#     square_of_three_room = serializers.FloatField(default=1)
#     number_of_four_room = serializers.IntegerField(default=1)
#     square_of_four_room = serializers.FloatField(default=1)
#     # ----------------------------------------------------

#     number_of_apartments_per_floor = serializers.IntegerField(default=1)  #
#     commercial_premises = serializers.IntegerField(default=1)  # пишешь только этаж
#     heating = fields.ChoiceFieldCustomDisplay(choices=choices.THE_HEATING_CHOICES, default=choices.NOT_COMPLETED,
#                                 # source='get_heating_display'
#                               )
#     gasification = serializers.BooleanField(default=1)
#     elevator = serializers.CharField(max_length=50,default=1)  #
#     parking = fields.ChoiceFieldCustomDisplay(choices=choices.THE_PARKING_CHOICES,default=choices.NOT_COMPLETED,)
#                                 # source='parking'
#     parking = fields.MultipleChoiceFieldCustomDisplay(choices=choices.THE_PARKING_CHOICES,default=choices.NOT_COMPLETED)
#     number_of_parking_spaces = serializers.IntegerField(default=1)
#     price = serializers.IntegerField(default=1)
#     completion_date = serializers.IntegerField(default=1)
#     description = serializers.CharField(default=1)

#     slug = serializers.SlugField(max_length=150)
#     lat = serializers.FloatField()
#     lng = serializers.FloatField()

#     building_images = BuildingImageSerializer(many=True)
#     layout_images = LayoutImageSerializer(many=True)
#     ways_from_metro = WayFromMetroSerializer(many=True)

# class StreetsSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     street_ru = serializers.CharField(max_length=200)
#     street_uk = serializers.CharField(max_length=200)

# class AdministrativeDistrictsSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     administrative_dist_ru = serializers.CharField(max_length=150)
#     administrative_dist_ukr = serializers.CharField(max_length=150)
#     administrative_old_dist_ru = serializers.CharField(max_length=150)
#     administrative_old_dist_urk = serializers.CharField(max_length=150)

# class DevelopersSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     developer_name = serializers.CharField(max_length=150)


#-------------------------------------- NEW VERSION!!!!!!

from rest_framework import serializers
from . import choices, fields, models

class ExtraFieldsMixin():
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return self.Meta.extra_fields + expanded_fields
        else:
            return expanded_fields

class StreetsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    street_ru = serializers.CharField(max_length=200)
    street_uk = serializers.CharField(max_length=200)

class AdministrativeDistrictsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    administrative_dist_ru = serializers.CharField(max_length=150)
    administrative_dist_ukr = serializers.CharField(max_length=150)
    administrative_old_dist_ru = serializers.CharField(max_length=150)
    administrative_old_dist_urk = serializers.CharField(max_length=150)

class DevelopersSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    developer_name = serializers.CharField(max_length=150)

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


class NewBuildingSerializerForSearch(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    street = serializers.SlugRelatedField(slug_field="street_ru",queryset=models.Street.objects.all())
    administrative_district = serializers.SlugRelatedField(slug_field="administrative_dist_ru",queryset=models.AdministrativeDistrict.objects.all())
    house_number = serializers.CharField(max_length=10)
    house_letter = serializers.CharField(max_length=1)
    district = fields.ChoiceFieldCustomDisplay(choices=choices.DISTRICT_CHOICES,
                                default=choices.NOT_COMPLETED,
                                # source='get_district_display'
                                )  # )
    micro_district = fields.ChoiceFieldCustomDisplay(choices=choices.FULL_MICRO_DISTRICT_CHOICES,
                                default=choices.MICRO_DISTRICT_DOES_NOT_EXIST,
                                # source='get_district_display'
                                )  # )
    developer = serializers.CharField(max_length=100, default=1)
    slug = serializers.CharField()
    building_images = BuildingImageSerializer(many=True)
    layout_images = LayoutImageSerializer(many=True)
    ways_from_metro = WayFromMetroSerializer(many=True)

class NewBuildingSerializer(serializers.ModelSerializer, ExtraFieldsMixin):
	street = serializers.SlugRelatedField(slug_field="street_ru",queryset=models.Street.objects.all())
	administrative_district = serializers.SlugRelatedField(slug_field="administrative_dist_ru",queryset=models.AdministrativeDistrict.objects.all())
	developer = serializers.SlugRelatedField(slug_field="developer_name",queryset=models.Developer.objects.all())
	ways_from_metro = WayFromMetroSerializer(many=True)
	building_images = BuildingImageSerializer(many=True)
	layout_images = LayoutImageSerializer(many=True)
	district = fields.ChoiceFieldCustomDisplay(choices=choices.DISTRICT_CHOICES, default=choices.NOT_COMPLETED)  
	micro_district = fields.ChoiceFieldCustomDisplay(choices=choices.FULL_MICRO_DISTRICT_CHOICES, default=choices.NOT_COMPLETED)
	construction_technology = fields.ChoiceFieldCustomDisplay(choices=choices.THE_CONSTRUCTION_TECHNOLOGY_CHOICES, default=choices.NOT_COMPLETED)
	heating = fields.ChoiceFieldCustomDisplay(choices=choices.THE_HEATING_CHOICES, default=choices.NOT_COMPLETED)
	parking = fields.MultipleChoiceFieldCustomDisplay(choices=choices.THE_PARKING_CHOICES, default=choices.NOT_COMPLETED)
	the_class = fields.ChoiceFieldCustomDisplay(choices=choices.THE_CLASS_CHOICES, default=choices.NOT_COMPLETED)
	
	class Meta:
		model = models.NewBuilding
		fields = '__all__'
		extra_fields = ['parking','district','micro_district','street','construction_technology','heating','the_class','construction_technology','administrative_district','developer','ways_from_metro','building_images','layout_images']
		lookup_field = 'slug'
		extra_kwargs = {
			'url': {'lookup_field': 'slug'}
		}
