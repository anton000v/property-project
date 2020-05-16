from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NewBuilding, AdministrativeDistrict, Street
from .serializers import NewBuildingSerializer, NewBuildingSerializerForSearch, StreetsSerializer, AdministrativeDistrictsSerializer
from . import choices
from django.http import JsonResponse, HttpResponse, Http404
from .utils import House
from django.http import Http404
import json

# class NewBuildingView(APIView):
#     def get(self, request):
#         buildings = NewBuilding.objects.all()
#         serializer = NewBuildingSerializer(buildings,many=True)
#         print("Data: ",serializer.data)
#         print("Type of data: ", type(serialserializers.CharField(max_length=200, default=1)izer.data))
#         print("Serializer: ", serializer)
#         return Response({"buildings": serializer.data})

class MicroDistrictChoices(APIView):
    def get(self,request):
        micro_district_choices = {}
        micro_district_choices['default'] = choices.MICRO_DISTRICT_DEFAULT_CHOICE + choices.MICRO_DISTRICT_DOES_NOT_EXIST_CHOICE
        micro_district_choices['saltovka'] = choices.MICRO_DISTRICT_SALTOVKA_CHOICES
        micro_district_choices['severnaya_saltovka'] = choices.MICRO_DISTRICT_SEVERNAYA_SALTOVKA_CHOICES
        # json_choices = json.dumps(micro_district_choices, ensure_ascii=False)
        db_values = {'saltovka_dbvalue' : choices.SALTOVKA, 'severnaya_saltovka_dbvalue': choices.SEVERNAYA_SALTOVKA}
        return JsonResponse({'micro_district_choices':micro_district_choices, 'db_values':db_values})



class GetBuilding(APIView):
    def get(self,request):
        slug = request.GET.get('slug')
        try:
            building = NewBuilding.objects.get(slug=slug)
            serializer = NewBuildingSerializer(building)
            return Response({'building':serializer.data})
        except NewBuilding.DoesNotExist:
            raise Http404

class FindBuildings(APIView):
    def get(self,request):
        # print("FIND BUILDINGS!!!!!!!!")
        buildings = NewBuilding.objects.all()
        found_buildings = set()
        # name_contains_query = request.GET.get('name')
        # address_contains_query = request.GET.get('address')
        # district_contains_query = request.GET.get('district')
        # developer_contains_query = request.GET.get('developer')

        districts_query_list = request.GET.getlist('district', '')
        streets_query_list = request.GET.getlist('street', '')
        administrative_districts_query_list = request.GET.getlist('administrative_district', '')
        house_number = request.GET.getlist('house_number', '')

        print(streets_query_list)
        
        if districts_query_list or streets_query_list or administrative_districts_query_list:
            if districts_query_list:
                for district_db_value in districts_query_list:
                    print('District db value for filter: ', district_db_value)
                    found_buildings = found_buildings.union(buildings.filter(district=district_db_value))

            if streets_query_list:
                for street_id in streets_query_list:
                    print('Street id for filter: ', street_id)
                    found_buildings = found_buildings.union(buildings.filter(street__id=street_id)) 

            if administrative_districts_query_list:
                for administrative_district_id in administrative_districts_query_list:
                    print('Administrative district id for filter: ', administrative_district_id)
                    found_buildings = found_buildings.union(buildings.filter(administrative_district__id=administrative_district_id)) 

        else:
            found_buildings = buildings

        serializer = NewBuildingSerializerForSearch(found_buildings,many=True)
        return Response({'buildings':serializer.data})

class AddressChecker(APIView):
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

                    response.status_code = 403 # To announce that the user isn't allowed to publish
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
                    response.status_code = 403 # To announce that the user isn't allowed to publish
                    return response
        else:
            raise Http404

class APIGetStreetsChoices(APIView):
    def get(self, request):
        streets = Street.objects.all()
        # print(streets)
        serializer = StreetsSerializer(streets, many=True)
        return Response({'streets':serializer.data})


class APIGetMicroDistrictsChoices(APIView):
    def get(self, request):
        db_value_field = 'db_value'
        text_value_field = 'text_value'
        if not len(choices.MICRO_DISTRICT_DOES_NOT_EXIST_CHOICE) == 1:
            raise Exception("Micro district default choice has more than 1 element!")
        def_choices = {
            db_value_field:choices.MICRO_DISTRICT_DOES_NOT_EXIST_CHOICE[0][0],
            text_value_field:choices.MICRO_DISTRICT_DOES_NOT_EXIST_CHOICE[0][1],
            }
        saltovka_micro_district_choices = [
             {db_value_field:element[0], text_value_field:element[1]} 
             for element in choices.MICRO_DISTRICT_SALTOVKA_CHOICES
             if len(element) == 2
             ]
        severnaya_saltovka_micro_district_choices = [
            {db_value_field:element[0], text_value_field:element[1]} 
             for element in choices.MICRO_DISTRICT_SEVERNAYA_SALTOVKA_CHOICES
             if len(element) == 2
        ]
        if not def_choices or not saltovka_micro_district_choices or not severnaya_saltovka_micro_district_choices:
            raise Exception("Micro district choices are empty")
        return Response({
            'micro_districts':{
            'not_divided':def_choices,
            'saltovka_micro_districts':saltovka_micro_district_choices,
            'severnaya_saltovka_micro_districts':severnaya_saltovka_micro_district_choices,
            }
        })

class APIGetDistrictsChoices(APIView):
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
                # d = {}
                # d['db_value'] = tup[0]
                # d['text_value'] = tup[1]
                # districts_choices.append(d)
        if not districts_choices:
            districts_choices.append({'districts':'empty districts :('})
        return Response({'districts':districts_choices})
        
        # all_districts = District.objects.all()
        # serializer = DistrictsSerializer(all_districts, many=True)
        # return Response({'districts':serializer.data})


class APIGetAdministrativeDistrictsChoices(APIView):
    def get(self, request):
        all_administrative_districts = AdministrativeDistrict.objects.all()
        serializer = AdministrativeDistrictsSerializer(all_administrative_districts, many=True)

        print('Get admin districts request!')
        return Response({'administrative_districts':serializer.data})
        # adm_districts = [{'db_val':value[0], 'administrative_district':value[1]} for value in list(choices.THE_ADMINISTRATIVE_DISTRICT_CHOICES)]
        # print('Send administrative districts choices')
        # return Response({'administrative_districts':adm_districts})

        