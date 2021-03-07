from rest_framework import serializers
from . import choices, fields, models
from nested_relations.serializers import NestedDataModelSerializer


class ExtraFieldsMixin():
    '''
        Может не нужно
    '''

    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return self.Meta.extra_fields + expanded_fields
        else:
            return expanded_fields


class StreetsSerializer(serializers.Serializer):
    ''' Сериализатор улицы для сериализатор новостроя'''
    id = serializers.IntegerField()
    street_ru = serializers.CharField(max_length=200)
    street_uk = serializers.CharField(max_length=200)


class AdministrativeDistrictsSerializer(serializers.Serializer):
    '''
    Сериализатор административного района для сериализатора новостроя
    '''
    id = serializers.IntegerField()
    administrative_dist_ru = serializers.CharField(max_length=150)
    administrative_dist_ukr = serializers.CharField(max_length=150)
    administrative_old_dist_ru = serializers.CharField(max_length=150)
    administrative_old_dist_urk = serializers.CharField(max_length=150)


class DevelopersSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    developer_name = serializers.CharField(max_length=150)


class WayFromMetroSerializer(serializers.Serializer):
    '''
    Сериализатор путей от метро для новостроя
    '''
    metro = fields.ChoiceFieldCustomDisplay(choices=choices.THE_METRO_CHOICES, default=choices.NOT_COMPLETED)
    type_of_movement = fields.ChoiceFieldCustomDisplay(choices=choices.THE_TYPE_OF_MOVEMENT_CHOICES,
                                                       default=choices.NOT_COMPLETED)
    time = serializers.IntegerField()
    number_of_meters = serializers.IntegerField()
    # class Meta:
    #     model = models.WayFromMetro
    #     fields = '__all__'


class BuildingImageSerializer(serializers.ModelSerializer):
    '''
        Сериализатор фотографий новостроя
    '''

    class Meta:
        model = models.BuildingImage
        fields = '__all__'


class LayoutImageSerializer(serializers.ModelSerializer):
    '''Сериализатор планировок  новостроя'''

    class Meta:
        model = models.LayoutImage
        fields = '__all__'


class FlatForSaleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FlatForSaleImage
        fields = ('flat_image',)


class FlatForSaleLayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FlatForSaleLayout
        fields = ('flat_layout',)


class FlatForSaleFromBuildingSerializer(serializers.ModelSerializer):
    '''Сериализатор квартир на продажу (для сериализатора новостроя)'''

    # building = serializers.SlugRelatedField(slug_field="slug",queryset=models.Street.objects.all())
    # floor = 
    # price
    # flat_images = FlatForSaleImageSerializer(many=True)
    # flat_layouts = FlatForSaleLayoutSerializer(many=True)
    class Meta:
        model = models.FlatForSale
        fields = ['id']


class NewBuildingSerializerForSearch(serializers.Serializer):
    '''Сериализатор новостроя для поиска (с уменьшинным кол-вом информации)'''

    name = serializers.CharField(max_length=200)
    street = serializers.SlugRelatedField(slug_field="street_ru", queryset=models.Street.objects.all())
    administrative_district = serializers.SlugRelatedField(slug_field="administrative_dist_ru",
                                                           queryset=models.AdministrativeDistrict.objects.all())
    house_number = serializers.CharField(max_length=10)
    house_letter = serializers.CharField(max_length=1)
    district = fields.ChoiceFieldCustomDisplay(choices=choices.DISTRICT_CHOICES,
                                               default=choices.NOT_COMPLETED,
                                               )
    micro_district = fields.ChoiceFieldCustomDisplay(choices=choices.FULL_MICRO_DISTRICT_CHOICES,
                                                     default=choices.MICRO_DISTRICT_DOES_NOT_EXIST,
                                                     # source='get_district_display'
                                                     )  # )
    developer = serializers.CharField(max_length=100, default=1)
    number_of_storeys = serializers.CharField(max_length=100, default=1)
    slug = serializers.CharField()
    lat = serializers.FloatField()
    lng = serializers.FloatField()
    building_images = BuildingImageSerializer(many=True)
    layout_images = LayoutImageSerializer(many=True)
    ways_from_metro = WayFromMetroSerializer(many=True)

    flats_for_sale = FlatForSaleFromBuildingSerializer(many=True)


class NewBuildingSerializer(serializers.ModelSerializer, ):
    '''Сериализатор отдельного новостроя'''

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

    flats_for_sale = FlatForSaleFromBuildingSerializer(many=True)

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


class NewBuildingForFlatSerializer(serializers.Serializer):
    '''Сериализатор новостроя (parent) для поиска квартиры (child)'''
    slug = serializers.CharField()
    street = serializers.SlugRelatedField(slug_field="street_ru", queryset=models.Street.objects.all())
    administrative_district = serializers.SlugRelatedField(slug_field="administrative_dist_ru",
                                                           queryset=models.AdministrativeDistrict.objects.all())
    house_number = serializers.IntegerField()
    house_letter = serializers.CharField(max_length=3)
    developer = serializers.SlugRelatedField(slug_field="developer_name", queryset=models.Developer.objects.all())
    ways_from_metro = WayFromMetroSerializer(many=True)
    district = fields.ChoiceFieldCustomDisplay(choices=choices.DISTRICT_CHOICES, default=choices.NOT_COMPLETED)
    micro_district = fields.ChoiceFieldCustomDisplay(choices=choices.FULL_MICRO_DISTRICT_CHOICES,
                                                     default=choices.NOT_COMPLETED)
    flats_for_sale = FlatForSaleFromBuildingSerializer(many=True)
    lat = serializers.FloatField()
    lng = serializers.FloatField()


class FlatForSaleForSearchSerializer(serializers.ModelSerializer):
    '''Сериализатор для поиска квартир'''
    # building = serializers.SlugRelatedField(slug_field="slug",queryset=models.NewBuilding.objects.all())
    # flats_for_sale = serializers.JSONField(required=False, allow_null=True)
    building = NewBuildingForFlatSerializer()
    flat_images = FlatForSaleImageSerializer(many=True)
    flat_layouts = FlatForSaleLayoutSerializer(many=True)

    class Meta:
        model = models.FlatForSale
        fields = '__all__'
        # nestedSerializer = {
        #     'building': {'serializer_class': NewBuildingSerializerForSearch, 'many': False, 'kwargs': 'content_object'},
        #     # 'skills':{'serializer_class': SkillSerializer, 'many': True, 'kwargs': 'person'}
        # }

# class FlatForSaleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.FlatForSale
#         fields = '__all__'
