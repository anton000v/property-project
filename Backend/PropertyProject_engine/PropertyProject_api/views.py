from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (
    NewBuilding,
    AdministrativeDistrict,
    Street,
    Developer
)
# from .models import AdministrativeDistrict 
# from .models import Street 
# from .models import Developer
from .serializers import ( 
    NewBuildingSerializer,
    NewBuildingSerializerForSearch,
    StreetsSerializer,
    AdministrativeDistrictsSerializer,
    DevelopersSerializer
)
# from .serializers import NewBuildingSerializerForSearch 
# from .serializers import StreetsSerializer 
# from .serializers import AdministrativeDistrictsSerializer
# from .serializers import DevelopersSerializer
from . import choices
from django.http import JsonResponse, HttpResponse, Http404
from .utils import House
from .utils import cartesian_product_dict
import json

#----------------- Main api views


#----------------- Support VIEWS
class MicroDistrictChoices(APIView):
    '''
    Класс для получения вариантов выбора микрорайона. Используется в админке для ajax js.
    '''
    def get(self,request):
        micro_district_choices = {}
        micro_district_choices['default'] = choices.MICRO_DISTRICT_DEFAULT_CHOICE + choices.MICRO_DISTRICT_DOES_NOT_EXIST_CHOICE
        micro_district_choices['saltovka'] = choices.MICRO_DISTRICT_SALTOVKA_CHOICES
        micro_district_choices['severnaya_saltovka'] = choices.MICRO_DISTRICT_SEVERNAYA_SALTOVKA_CHOICES
        db_values = {'saltovka_dbvalue' : choices.SALTOVKA, 'severnaya_saltovka_dbvalue': choices.SEVERNAYA_SALTOVKA}
        return JsonResponse({'micro_district_choices':micro_district_choices, 'db_values':db_values})


class AddressChecker(APIView):
    '''
    Класс для проверки правильности введенного адреса. Используется в админке.
    '''
    def get(self,request):
        # print("Ajax request is accepted")
        if request.is_ajax():
            street = request.GET.get('street', None)
            house_number = request.GET.get('house_number', None)
            house_letter = request.GET.get('house_letter', None)
            type = request.GET.get('type')

            if type == 'house_number':
                house = House(street=street, house_number=house_number)
                if house.is_exist(with_letter=False):
                    house.fill_district()
                    response = JsonResponse({"success_message": 'Номер дома существует!','choices':choices.HOUSE_LETTER_CHOICES})
                    return response

                else:
                    response = JsonResponse({"error": 'Дом на улице "{}" под номером "{}" не найден в {}е'.format(house.street,
                                                                                                                 house.house_number,
                                                                                                                 house.city),
                                            'choices':choices.HOUSE_LETTER_CHOICES
                                                                                                                 })

                    response.status_code = 403 
                    return response

            elif type == 'house_letter':
                house = House(street=street, house_number=house_number, house_letter=house_letter)
                if house.is_exist():
                    house.fill_district()
                    house.fill_location()
                    pure_district = house.house_district.split()[0]
                    administrative_district_id = AdministrativeDistrict.objects.get(administrative_dist_ukr=pure_district).id
                    
                    response = {
                    'success_message': 'Дом существует',
                    'administrative_district_id': administrative_district_id,
                    'lat' : house.lat,
                    'lng' : house.lng,
                    }
                    return JsonResponse(response)
                else:
                    response = JsonResponse(
                        {"error": '"{}, {}{}" не найдено в {}е'.format(house.street,
                                                                  house.house_number,
                                                                  house.house_letter,
                                                                  house.city)
                                                                  })
                    response.status_code = 403 
                    return response
        else:
            raise Http404


class APIGetStreetsChoices(APIView):
    '''
    Класс для получения вариантов выбора улиц. Используется фронтендом.
    '''
    def get(self, request):
        streets = Street.objects.all()
        # print(streets)
        serializer = StreetsSerializer(streets, many=True)
        return Response({'streets':serializer.data})

class APIGetSaltovkaMicroDistrictsChoices(APIView):
    '''
    Класс для получения вариантов выбора микрорайонов салтовки. Используется фронтендом.
    '''
    def get(self, request):
        db_value_field = 'db_value'
        text_value_field = 'text_value'
        saltovka_micro_district_choices = [
             {db_value_field:element[0], text_value_field:element[1]} 
             for element in choices.MICRO_DISTRICT_SALTOVKA_CHOICES
             if len(element) == 2
             ]  
        if not saltovka_micro_district_choices:
            raise Exception("Saltovka micro district choices is empty")
        return Response({'saltovka_micro_districts':saltovka_micro_district_choices})

class APIGetSevernayaSaltovkaMicroDistrictsChoices(APIView):
    '''
    Класс для получения вариантов выбора микрорайонов северной салтовки. Используется фронтендом.
    '''
    def get(self, request):
        db_value_field = 'db_value'
        text_value_field = 'text_value'
        severnaya_saltovka_micro_district_choices = [
            {db_value_field:element[0], text_value_field:element[1]} 
             for element in choices.MICRO_DISTRICT_SEVERNAYA_SALTOVKA_CHOICES
             if len(element) == 2
        ]
        if not severnaya_saltovka_micro_district_choices:
            raise Exception("Severnaya Saltovka micro district choices is empty")
        return Response({'severnaya_saltovka_micro_districts':severnaya_saltovka_micro_district_choices})

class APIGetDistrictsChoices(APIView):
    '''
    Класс для получения вариантов выбора районов. Используется фронтендом.
    '''
    def get(self, request):
        districts_choices = []
        for tup in choices.DISTRICT_CHOICES:
            if (type(tup[1]) is tuple) or (
                type(tup[1]) is list) or (
                type(tup[1]) is dict):
                for district in tup[1]:
                    d = {}
                    d['direction'] = tup[0]
                    d['db_value'] = district[0]
                    d['text_value'] = district[1]
                    districts_choices.append(d)
            else :
                continue
        if not districts_choices:
            raise Exception("District choices is empty")
        return Response({'districts':districts_choices})
        

class APIGetAdministrativeDistrictsChoices(APIView):
    '''
    Класс для получения вариантов выбора административных районов. Используется фронтендом.
    '''
    def get(self, request):
        all_administrative_districts = AdministrativeDistrict.objects.all()
        serializer = AdministrativeDistrictsSerializer(all_administrative_districts, many=True)
        # print('Get admin districts request!')
        return Response({'administrative_districts':serializer.data})


class APIGetSaltovkaSevernayaSaltovkaDBValues(APIView):
    '''
    Класс для получения буквенных значений, которые представляют Салтовку и Северную Салтовку в бд. 
    Используется фронтендом.
    '''
    def get(self, request):
        return Response({
            'saltovka_db_value':choices.SALTOVKA,
            'severnaya_saltovka_db_value':choices.SEVERNAYA_SALTOVKA,
        })

class APIGetDevelopersChoices(APIView):
    '''
    Класс для получения вариантов выбора застройщиков. Используется фронтендом.
    '''
    def get(self, request):
        all_developers = Developer.objects.all()
        serializer = DevelopersSerializer(all_developers, many = True)
        return Response({'developers':serializer.data})

class APIGetMetroChoices(APIView):
    '''
    Класс для получения вариантов выбора метро. Используется фронтендом.
    '''
    def get(self, request):
        metro_choices = []
        db_value_field = 'db_value'
        text_value_field = 'text_value'
        for tup in choices.THE_METRO_CHOICES:
                if (type(tup[1]) is tuple) or (
                    type(tup[1]) is list) or (
                    type(tup[1]) is dict):
                    for metro in tup[1]:
                        m = {}
                        m['line'] = tup[0]
                        m['db_value'] = metro[0]
                        m['text_value'] = metro[1]
                        metro_choices.append(m)
                else :
                    continue
        if not metro_choices:
            raise Exception("Metro choices is empty")
        return Response({'metro':metro_choices})

class APIGetClassChoices(APIView):
    '''
    Класс для получения вариантов выбора класса. Используется фронтендом.
    '''
    def get(self, request):
        class_choices = [{ 'db_value':item[0], 'text_value': item[1] } for item in choices.THE_CLASS_CHOICES[1:] ]
        if(not class_choices):
            raise Exception('Class choices is empty')
        return Response({'classes':class_choices})

class APIGetWallsTypesChoices(APIView):
    '''
    Класс для получения вариантов выбора типа стен. Используется фронтендом. 
    '''
    def get(self, request):
        walls_type_choices = [{ 'db_value':item[0], 'text_value': item[1] } for item in choices.THE_WALLS_TYPE_CHOICES[1:] ]
        if(not walls_type_choices):
            raise Exception('Walls type choices is empty')
        return Response({'walls_types':walls_type_choices})

class APIGetWarmingTypesChoices(APIView):
    '''
    Класс для получения варинтов выбора утепления. Используется фронтендом
    '''
    def get(self, request):
        warming_types_choices = [{ 'db_value':item[0], 'text_value': item[1] } for item in choices.THE_WARMING_CHOICES[1:] ]
        if(not warming_types_choices):
            raise Exception('Warming types choices is empty')
        return Response({'warming_types_choices':warming_types_choices})

class APIGetHeatingTypesChoices(APIView):
    '''
    Класс для получения варинтов выбора отопления. Используется фронтендом
    '''
    def get(self, request):
        heating_types_choices = [{ 'db_value':item[0], 'text_value': item[1] } for item in choices.THE_HEATING_CHOICES[1:] ]
        if(not heating_types_choices):
            raise Exception('Heating types choices is empty')
        return Response({'heating_types_choices':heating_types_choices})

class APIGetParkingTypesChoices(APIView):
    '''
    Класс для получения варинтов выбора парковки. Используется фронтендом
    '''
    def get(self, request):
        parking_types_choices = [{ 'db_value':item[0], 'text_value': item[1] } for item in choices.THE_HEATING_CHOICES[1:] ]
        if(not parking_types_choices):
            raise Exception('Parking types choices is empty')
        return Response({'parking_types_choices':parking_types_choices})

# class APIGetBuilding(APIView):
#     def get(self,request):
#         slug = request.GET.get('slug')
#         try:
#             building = NewBuilding.objects.get(slug=slug)
#             serializer = NewBuildingSerializer(building)
#             return Response({'building':serializer.data})
#         except NewBuilding.DoesNotExist:
#             raise Http404
     

# VERSION 2
# class APIFindBuildings(APIView):
#     def get(self, request):
#         print('OK. Get buidings begin')
#         found_buildings = set()
#         districts_query_list = request.GET.getlist('district', '')
#         streets_query_list = request.GET.getlist('street', '')
#         administrative_districts_query_list = request.GET.getlist('administrative_district', '')
#         house_numbers_query_list = request.GET.getlist('house_number', '')
#         saltovka_microdistricts_query_list = request.GET.getlist('saltovka_microdistrict', '')
#         severnaya_saltovka_microdistricts_query_list = request.GET.getlist('severnaya_saltovka_microdistrict', '')
#         developers_query_list = request.GET.getlist('developer', '')


#         #---------- Searchable block
#         if districts_query_list or streets_query_list or administrative_districts_query_list:
#             if streets_query_list:
#                 if house_numbers_query_list:
#                     print(house_numbers_query_list)
#                     for result in self.get_buildings_by(
#                         street=streets_query_list,
#                         house_number=house_numbers_query_list
#                         ):
#                         found_buildings = found_buildings.union(result)   
#                 else:
#                     for result in self.get_buildings_by(street=streets_query_list):
#                         found_buildings = found_buildings.union(result)   


#             if districts_query_list:
#                 if saltovka_microdistricts_query_list:
#                     for result in self.get_buildings_by(
#                         district=choices.SALTOVKA.split(),
#                         micro_district=saltovka_microdistricts_query_list
#                         ):
#                         districts_query_list.remove(choices.SALTOVKA)
#                         found_buildings = found_buildings.union(result) 
#                 if severnaya_saltovka_microdistricts_query_list:
#                     for result in self.get_buildings_by(
#                         district=choices.SEVERNAYA_SALTOVKA.split(),
#                         micro_district=severnaya_saltovka_microdistricts_query_list
#                         ):
#                         districts_query_list.remove(choices.SEVERNAYA_SALTOVKA)
#                         found_buildings = found_buildings.union(result) 
#                 for result in self.get_buildings_by(district=districts_query_list):
#                     found_buildings = found_buildings.union(result)
    
#             if administrative_districts_query_list:
#                 for result in self.get_buildings_by(administrative_district=administrative_districts_query_list):
#                     found_buildings = found_buildings.union(result) 
#         else:
#             found_buildings = NewBuilding.objects.all()

#         serializer = NewBuildingSerializerForSearch(found_buildings, many = True)
#         return Response({"buildings":serializer.data})


#     def get_buildings_by(self, **kwargs):
#         for query in cartesian_product_dict(**kwargs):
#             print('Поисковой Запрос: ', query)
#             yield NewBuilding.objects.filter(**query)

#     def filter_buildings_by(self, found_buildings , **kwargs):
#        for query in cartesian_product_dict(**kwargs):
#             print('Фильтр запрос: ', query)
#             yield found_buildings.filter(**query)

# Version 1
# class FindBuildings(APIView):
#     def get(self,request):
#         print("FIND BUILDINGS!!!!!!!!")
#         buildings = NewBuilding.objects.all()
#         found_buildings = set()
#         districts_query_list = request.GET.getlist('district', '')
#         streets_query_list = request.GET.getlist('street', '')
#         administrative_districts_query_list = request.GET.getlist('administrative_district', '')
#         house_numbers_query_list = request.GET.getlist('house_number', '')
#         saltovka_microdistricts_query_list = request.GET.getlist('saltovka_microdistrict', '')
#         severnaya_saltovka_microdistricts_query_list = request.GET.getlist('severnaya_saltovka_microdistrict', '')
#         # developers_query_list = request.GET.getlist('developer', '')

#         if (
#             districts_query_list or 
#             streets_query_list or 
#             administrative_districts_query_list
#             # developers_query_list
#             ):
#             if districts_query_list:       
#                 if saltovka_microdistricts_query_list:
#                     for microdistrict in saltovka_microdistricts_query_list:
#                         try:
#                             found_buildings = found_buildings.union(buildings.filter(
#                                 district=districts_query_list.pop(districts_query_list.index(choices.SALTOVKA)),
#                                 micro_district=microdistrict)
#                                 )
#                         except (IndexError, ValueError) as e:
#                             print(e)
#                             break 
#                 if severnaya_saltovka_microdistricts_query_list:
#                     for microdistrict in severnaya_saltovka_microdistricts_query_list:
#                         try:
#                             found_buildings = found_buildings.union(buildings.filter(
#                                 district=districts_query_list.pop(districts_query_list.index(choices.SEVERNAYA_SALTOVKA)),
#                                 micro_district=microdistrict)
#                                 )
#                         except (IndexError, ValueError) as e:
#                             print(e)
#                             break 

#                 for district_db_value in districts_query_list:
#                     print('District db value for filter: ', district_db_value)
#                     found_buildings = found_buildings.union(buildings.filter(district=district_db_value))

#             if streets_query_list:
#                 for street_id in streets_query_list:   
#                     if house_numbers_query_list:
#                         for house_number in house_numbers_query_list:
#                             print('Street id for filter: {} | house number: {}'.format(street_id, house_number))
#                             found_buildings = found_buildings.union(buildings.filter(street__id=street_id,house_number=house_number))
#                     else:
#                         print('Street id for filter: ', street_id)        
#                         found_buildings = found_buildings.union(buildings.filter(street__id=street_id)) 

#             if administrative_districts_query_list:
#                 for administrative_district_id in administrative_districts_query_list:
#                     print('Administrative district id for filter: ', administrative_district_id)
#                     found_buildings = found_buildings.union(buildings.filter(administrative_district__id=administrative_district_id)) 
            
#             # if developers_query_list:
#             #     for developer_id in developers_query_list:
#             #         print('Developers id for filter: ', developer_id)
#             #         found_buildings = found_buildings.union(buildings.filter(administrative_district__id=administrative_district_id))
#         else:
#             found_buildings = buildings

#         serializer = NewBuildingSerializerForSearch(found_buildings,many=True)
#         return Response({'buildings':serializer.data})

# class AddressChecker(APIView):
#     def get(self,request):
#         # print("Ajax request is accepted")
#         if request.is_ajax():
#             street = request.GET.get('street', None)
#             house_number = request.GET.get('house_number', None)
#             house_letter = request.GET.get('house_letter', None)
#             type = request.GET.get('type')

#             if type == 'house_number':
#                 house = House(street=street, house_number=house_number)
#                 if house.is_exist(with_letter=False):
#                     house.fill_district()
#                     response = JsonResponse({"success_message": 'Номер дома существует!','choices':choices.HOUSE_LETTER_CHOICES})
#                     return response

#                 else:
#                     response = JsonResponse({"error": 'Дом на улице "{}" под номером "{}" не найден в {}е'.format(house.street,
#                                                                                                                  house.house_number,
#                                                                                                                  house.city),
#                                             'choices':choices.HOUSE_LETTER_CHOICES
#                                                                                                                  })

#                     response.status_code = 403 
#                     return response

#             elif type == 'house_letter':
#                 house = House(street=street, house_number=house_number, house_letter=house_letter)
#                 if house.is_exist():
#                     house.fill_district()
#                     house.fill_location()
#                     pure_district = house.house_district.split()[0]
#                     administrative_district_id = AdministrativeDistrict.objects.get(administrative_dist_ukr=pure_district).id
                    
#                     response = {
#                     'success_message': 'Дом существует',
#                     'administrative_district_id': administrative_district_id,
#                     'lat' : house.lat,
#                     'lng' : house.lng,
#                     }
#                     return JsonResponse(response)
#                 else:
#                     response = JsonResponse(
#                         {"error": '"{}, {}{}" не найдено в {}е'.format(house.street,
#                                                                   house.house_number,
#                                                                   house.house_letter,
#                                                                   house.city)
#                                                                   })
#                     response.status_code = 403 
#                     return response
#         else:
#             raise Http404
