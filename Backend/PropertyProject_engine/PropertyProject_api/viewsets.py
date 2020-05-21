from PropertyProject_api.models import Street, AdministrativeDistrict, Developer, NewBuilding
from .serializers import NewBuildingSerializer, NewBuildingSerializerForSearch
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from django.db.models import Q
import re 
import operator
from functools import reduce

BOOLEAN_CHOICES = (('false', 'False'), ('true', 'True'),)

# class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
#     pass

class NewBuildingFilter(filters.FilterSet):
    developer = filters.ModelMultipleChoiceFilter(
        field_name = 'developer',
        to_field_name = 'id',
        queryset = Developer.objects.all(),
    )
    developer = filters.ModelMultipleChoiceFilter(
        field_name = 'developer',
        to_field_name = 'id',
        queryset = Developer.objects.all(),
    )
    # street = NumberInFilter(field_name='street__id', lookup_expr='in')
    # street = filters.ModelMultipleChoiceFilter(
    #     field_name='street',
    #     to_field_name='id',
    #     queryset=Street.objects.all(),
    # )
    # administrative_district = filters.ModelMultipleChoiceFilter(
    #     field_name='administrative_district',
    #     to_field_name='id',
    #     queryset=AdministrativeDistrict.objects.all(),
    # )
    # flag = filters.TypedChoiceFilter(choices=BOOLEAN_CHOICES,)
                                            # coerce=strtobool)
    class Meta:
        model = NewBuilding
        fields = ['developer',]
        # fields = {
        #     'street' : ['icontains']
        # }

class NewBuildingViewSet(viewsets.ReadOnlyModelViewSet):
    #list create retrieve update partial_update destroy

    model = NewBuilding
    serializer_class = NewBuildingSerializerForSearch
    filterset_class = NewBuildingFilter
    lookup_field = 'slug'
    action_serializers = {
        'retrieve': NewBuildingSerializer,
        # 'list': MyModelListSerializer,
        # 'create': MyModelCreateSerializer
    }
    pagination_class =  PageNumberPagination
    
    def get_serializer_class(self):
        '''
        Метод, который возвращает класс сериализатора. 
        Переопределяем, чтобы для разных действий были разные сериализаторы
        '''

        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(MyModelViewSet, self).get_serializer_class()

    def get_queryset(self):
        '''
        Метод генерирующий первоначальный queryset.
        Переопределяем, добавляя возможность генерации с условиями поиска с помощью данных в GET запросе.
        '''

        districts_query_list = self.request.query_params.getlist('district', '')
        streets_query_list = self.request.query_params.getlist('street', '')
        administrative_districts_query_list = self.request.query_params.getlist('administrative_district', '')
        house_numbers_query_list = self.request.query_params.getlist('house_number', '')
        saltovka_microdistricts_query_list = self.request.query_params.getlist('saltovka_microdistrict', '')
        severnaya_saltovka_microdistricts_query_list = self.request.query_params.getlist('severnaya_saltovka_microdistrict', '')

        q_administrative_districts = Q()
        if administrative_districts_query_list:
            q_administrative_districts = Q(administrative_district__in = administrative_districts_query_list)
            print('Административные районы: ', administrative_districts_query_list)

        q_districts = Q()
        if districts_query_list:
            q_districts = Q(district__in=districts_query_list)
            print('Районы: ', districts_query_list)

        q_streets = Q()
        if streets_query_list:
            q_streets = Q(street__in=streets_query_list)
            print('Улицы: ', streets_query_list)

        q_house_numbers = Q()
        if house_numbers_query_list:
            # Парсинг номеров домов в списке (вида 23г, 25) в генератор кортежей вида (('23', 'г'), (25, ''))
            house_numbers_and_letters_generator = (
                (match.group(0), item[match.end():].upper()) for
                item in house_numbers_query_list
                if (match := re.match('\d+', item))
            )
            # Совмещение sql запросов с помощью оператора or
            q_house_numbers = reduce(
                operator.or_,
                (Q(house_number = number, house_letter=letter) for
                number, letter in 
                house_numbers_and_letters_generator
                )
            )
            print('Номера домов: ', house_numbers_and_letters_generator)

        q_saltovka_microdistricts = Q()
        q_severnaya_saltovka_microdistricts = Q()
        if saltovka_microdistricts_query_list:
            q_saltovka_microdistricts = Q(micro_district__in=saltovka_microdistricts_query_list)
        if severnaya_saltovka_microdistricts_query_list:
            q_severnaya_saltovka_microdistricts = Q(micro_district__in=severnaya_saltovka_microdistricts_query_list)
            
        found_buildings = NewBuilding.objects.filter(
            (q_streets & q_house_numbers) |  
            (q_districts & q_saltovka_microdistricts & q_severnaya_saltovka_microdistricts) | 
            q_administrative_districts
            )

        print('\t NASHLO: ',found_buildings)
        return found_buildings
