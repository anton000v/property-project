import re
import operator
from functools import reduce
from rest_framework import viewsets
from django_filters import rest_framework as filters
from django.db.models import Q
from .pagination import CustomPageNumber
from . import choices

from api.models import (
    Developer,
    NewBuilding,
    FlatForSale
)
from .serializers import (
    NewBuildingSerializer,
    NewBuildingSerializerForSearch,
    FlatForSaleForSearchSerializer
)

BOOLEAN_CHOICES = (('false', 'False'), ('true', 'True'),)


class BuildingFiltersMixin(filters.FilterSet):
    developer = filters.ModelMultipleChoiceFilter(
        field_name='developer',
        to_field_name='id',
        queryset=Developer.objects.all(),
        distinct=True
    )
    metro = filters.MultipleChoiceFilter(
        field_name='ways_from_metro__metro',
        # to_field_name = 'metro',
        choices=choices.THE_METRO_CHOICES,
        distinct=True
    )
    time_from_metro = filters.NumberFilter(
        field_name='ways_from_metro__time',
        lookup_expr='lte',
        distinct=True
    )
    the_class = filters.MultipleChoiceFilter(
        # field_name = 'ways_from_metro__metro',
        # to_field_name = 'metro',
        choices=choices.THE_CLASS_CHOICES,
        distinct=True
    )
    number_of_storeys_from = filters.NumberFilter(
        field_name='number_of_storeys',
        lookup_expr='gte',
        distinct=True
    )
    number_of_storeys_to = filters.NumberFilter(
        field_name='number_of_storeys',
        lookup_expr='lte',
        distinct=True
    )
    room_height_from = filters.NumberFilter(
        field_name='room_height',
        lookup_expr='gte',
        distinct=True
    )
    room_height_to = filters.NumberFilter(
        field_name='room_height',
        lookup_expr='lte',
        distinct=True
    )

    walls_type = filters.MultipleChoiceFilter(
        choices=choices.THE_WALLS_TYPE_CHOICES,
        distinct=True
    )

    heating = filters.MultipleChoiceFilter(
        choices=choices.THE_HEATING_CHOICES,
        distinct=True
    )

    warming = filters.MultipleChoiceFilter(
        choices=choices.THE_WARMING_CHOICES,
        distinct=True
    )


class NewBuildingFilter(BuildingFiltersMixin, filters.FilterSet):
    '''
    Класс отвечающий за фильтрацию Новостроев
    '''

    # developer = filters.ModelMultipleChoiceFilter(
    #     field_name='developer',
    #     to_field_name='id',
    #     queryset=Developer.objects.all(),
    #     distinct=True
    # )
    # metro = filters.MultipleChoiceFilter(
    #     field_name='ways_from_metro__metro',
    #     # to_field_name = 'metro',
    #     choices=choices.THE_METRO_CHOICES,
    #     distinct=True
    # )
    # time_from_metro = filters.NumberFilter(
    #     field_name='ways_from_metro__time',
    #     lookup_expr='lte',
    #     distinct=True
    # )
    # the_class = filters.MultipleChoiceFilter(
    #     # field_name = 'ways_from_metro__metro',
    #     # to_field_name = 'metro',
    #     choices=choices.THE_CLASS_CHOICES,
    #     distinct=True
    # )
    # number_of_storeys_from = filters.NumberFilter(
    #     field_name='number_of_storeys',
    #     lookup_expr='gte',
    #     distinct=True
    # )
    # number_of_storeys_to = filters.NumberFilter(
    #     field_name='number_of_storeys',
    #     lookup_expr='lte',
    #     distinct=True
    # )
    # room_height_from = filters.NumberFilter(
    #     field_name='room_height',
    #     lookup_expr='gte',
    #     distinct=True
    # )
    # room_height_to = filters.NumberFilter(
    #     field_name='room_height',
    #     lookup_expr='lte',
    #     distinct=True
    # )

    # walls_type = filters.MultipleChoiceFilter(
    #     choices=choices.THE_WALLS_TYPE_CHOICES,
    #     distinct=True
    # )
    #
    # heating = filters.MultipleChoiceFilter(
    #     choices=choices.THE_HEATING_CHOICES,
    #     distinct=True
    # )

    class Meta:
        model = NewBuilding
        fields = ['developer', 'metro', 'time_from_metro', 'the_class', 'number_of_storeys_from',
                  'number_of_storeys_to', 'room_height_from', 'room_height_to', 'walls_type', 'heating', 'warming']
        # fields = {
        #     'street' : ['icontains']
        # }


class FlatForSaleFilter(BuildingFiltersMixin, filters.FilterSet):
    '''
    Класс отвечающий за фильтрацию квартир
    '''
    # developer = filters.ModelMultipleChoiceFilter(
    #     field_name='building__developer',
    #     to_field_name='id',
    #     queryset=Developer.objects.all(),
    #     distinct=True
    # )
    # metro = filters.MultipleChoiceFilter(
    #     field_name='building__ways_from_metro__metro',
    #     # to_field_name = 'metro',
    #     choices=choices.THE_METRO_CHOICES,
    #     distinct=True
    # )
    # time_from_metro = filters.NumberFilter(
    #     field_name='building__ways_from_metro__time',
    #     lookup_expr='lte',
    #     distinct=True
    # )
    # the_class = filters.MultipleChoiceFilter(
    #     field_name='building__the_class',
    #     # to_field_name = 'metro',
    #     choices=choices.THE_CLASS_CHOICES,
    #     distinct=True
    # )
    floor_from = filters.NumberFilter(
        field_name='floor',
        lookup_expr='gte',
        distinct=True
    )
    floor_to = filters.NumberFilter(
        field_name='floor',
        lookup_expr='lte',
        distinct=True
    )
    rooms_from = filters.NumberFilter(
        field_name='rooms',
        lookup_expr='gte',
        distinct=True
    )
    rooms_to = filters.NumberFilter(
        field_name='rooms',
        lookup_expr='lte',
        distinct=True
    )
    price_from = filters.NumberFilter(
        field_name='price',
        lookup_expr='gte',
        distinct=True
    )
    price_to = filters.NumberFilter(
        field_name='price',
        lookup_expr='lte',
        distinct=True
    )

    # number_of_storeys_from = filters.NumberFilter(
    #     field_name='building__number_of_storeys',
    #     lookup_expr='gte',
    #     distinct=True
    # )
    # number_of_storeys_to = filters.NumberFilter(
    #     field_name='building__number_of_storeys',
    #     lookup_expr='lte',
    #     distinct=True
    # )
    # room_height_from = filters.NumberFilter(
    #     field_name='building__room_height',
    #     lookup_expr='gte',
    #     distinct=True
    # )
    # room_height_to = filters.NumberFilter(
    #     field_name='building__room_height',
    #     lookup_expr='lte',
    #     distinct=True
    # )
    # walls_type = filters.MultipleChoiceFilter(
    #     choices=choices.THE_WALLS_TYPE_CHOICES,
    #     distinct=True
    # )
    # heating = filters.MultipleChoiceFilter(
    #     choices=choices.THE_HEATING_CHOICES,
    #     distinct=True
    # )

    class Meta:
        model = FlatForSale
        fields = [
            'developer', 'metro', 'time_from_metro', 'the_class', 'floor_from', 'floor_to', 'rooms_from', 'rooms_to',
            'price_from', 'price_to',
            'number_of_storeys_from', 'number_of_storeys_to', 'room_height_from', 'room_height_to', 'walls_type',
            'heating', 'warming'
        ]


class NewBuildingViewSet(viewsets.ReadOnlyModelViewSet):
    # list create retrieve update partial_update destroy

    model = NewBuilding
    serializer_class = NewBuildingSerializerForSearch
    filterset_class = NewBuildingFilter
    lookup_field = 'slug'
    action_serializers = {
        'retrieve': NewBuildingSerializer,
        # 'list': MyModelListSerializer,
        # 'create': MyModelCreateSerializer
    }
    pagination_class = CustomPageNumber

    def get_serializer_class(self):
        '''
        Метод, который возвращает класс сериализатора. 
        Переопределяем, чтобы для разных действий были разные сериализаторы
        '''

        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(NewBuildingViewSet, self).get_serializer_class()

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
        severnaya_saltovka_microdistricts_query_list = self.request.query_params.getlist(
            'severnaya_saltovka_microdistrict', '')
        is_sallable_only = self.request.query_params.get('sallable_only', '')

        # print('\n\tSALLABLE ONLY: ', is_sallable_only)

        if districts_query_list or streets_query_list or administrative_districts_query_list or house_numbers_query_list or saltovka_microdistricts_query_list or severnaya_saltovka_microdistricts_query_list or is_sallable_only:
            q_administrative_districts = Q()
            if administrative_districts_query_list:
                q_administrative_districts = Q(administrative_district__in=administrative_districts_query_list)
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
                letter_or_none = lambda x: x or None
                # q_house_numbers = Q()
                # for number, letter in house_numbers_and_letters_generator:
                #     if letter:=letter_or_none(letter):
                #         q_house_numbers
                # Совмещение sql запросов с помощью оператора or
                q_house_numbers = reduce(
                    operator.or_,
                    (Q(house_number=number, house_letter=letter_or_none(letter)) for
                     number, letter in
                     house_numbers_and_letters_generator
                     )
                )
                print('Номера домов: ', house_numbers_query_list)

            q_saltovka_microdistricts = Q()
            q_severnaya_saltovka_microdistricts = Q()
            if saltovka_microdistricts_query_list:
                q_saltovka_microdistricts = Q(micro_district__in=saltovka_microdistricts_query_list)
            if severnaya_saltovka_microdistricts_query_list:
                q_severnaya_saltovka_microdistricts = Q(micro_district__in=severnaya_saltovka_microdistricts_query_list)

            q_sallable_only = Q()
            if is_sallable_only:
                q_sallable_only = Q(flats_for_sale__isnull=False)

            found_buildings = NewBuilding.objects.filter(
                q_sallable_only & (
                        (q_streets & q_house_numbers) |
                        (
                                q_districts & q_saltovka_microdistricts & q_severnaya_saltovka_microdistricts & q_house_numbers) |
                        q_administrative_districts
                )
            ).distinct()

            print('\t С ФИЛЬТРАЦИЕЙ: ', found_buildings)
            return found_buildings
        else:
            print('\t ВСЕ ОБЬЕКТЫ: ', NewBuilding.objects.all())
            # print('\tCount:', NewBuilding.objects.all())
            return NewBuilding.objects.all()

    class Meta:
        ordering = ['-id']


class FlatForSaleViewset(viewsets.ReadOnlyModelViewSet):
    model = FlatForSale
    serializer_class = FlatForSaleForSearchSerializer
    filterset_class = FlatForSaleFilter
    lookup_field = 'id'
    # action_serializers = {
    #     'retrieve': NewBuildingSerializer,
    #     # 'list': MyModelListSerializer,
    #     # 'create': MyModelCreateSerializer
    # }
    pagination_class = CustomPageNumber

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
        severnaya_saltovka_microdistricts_query_list = self.request.query_params.getlist(
            'severnaya_saltovka_microdistrict', '')

        if districts_query_list or streets_query_list or administrative_districts_query_list or house_numbers_query_list or saltovka_microdistricts_query_list or severnaya_saltovka_microdistricts_query_list:
            q_administrative_districts = Q()
            if administrative_districts_query_list:
                q_administrative_districts = Q(
                    building__administrative_district__in=administrative_districts_query_list)
                print('Административные районы: ', administrative_districts_query_list)

            q_districts = Q()
            if districts_query_list:
                q_districts = Q(building__district__in=districts_query_list)
                print('Районы: ', districts_query_list)

            q_streets = Q()
            if streets_query_list:
                q_streets = Q(building__street__in=streets_query_list)
                print('Улицы: ', streets_query_list)

            q_house_numbers = Q()
            if house_numbers_query_list:
                # Парсинг номеров домов в списке (вида 23г, 25) в генератор кортежей вида (('23', 'г'), (25, ''))
                house_numbers_and_letters_generator = (
                    (match.group(0), item[match.end():].upper()) for
                    item in house_numbers_query_list
                    if (match := re.match('\d+', item))
                )
                letter_or_none = lambda x: x or None
                # q_house_numbers = Q()
                # for number, letter in house_numbers_and_letters_generator:
                #     if letter:=letter_or_none(letter):
                #         q_house_numbers
                # Совмещение sql запросов с помощью оператора or
                q_house_numbers = reduce(
                    operator.or_,
                    (Q(building__house_number=number, building__house_letter=letter_or_none(letter)) for
                     number, letter in
                     house_numbers_and_letters_generator
                     )
                )
                print('Номера домов: ', house_numbers_query_list)

            q_saltovka_microdistricts = Q()
            q_severnaya_saltovka_microdistricts = Q()
            if saltovka_microdistricts_query_list:
                q_saltovka_microdistricts = Q(building__micro_district__in=saltovka_microdistricts_query_list)
            if severnaya_saltovka_microdistricts_query_list:
                q_severnaya_saltovka_microdistricts = Q(
                    building__micro_district__in=severnaya_saltovka_microdistricts_query_list)

            found_buildings = FlatForSale.objects.filter(
                (q_streets & q_house_numbers) |
                (q_districts & q_saltovka_microdistricts & q_severnaya_saltovka_microdistricts & q_house_numbers) |
                q_administrative_districts
            )

            print('\t Found: ', found_buildings)
            return found_buildings
        else:
            # print('\t NASHLO: ',FlatForSale.objects.all())
            # print('\tCount:', FlatForSale.objects.all())
            return FlatForSale.objects.all()
        # return  FlatForSale.objects.all()
