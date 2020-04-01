from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NewBuilding, District
from .serializers import NewBuildingSerializer
from . import choices
from django.http import JsonResponse, HttpResponse, Http404
from .utils import House
import json

# class NewBuildingView(APIView):
#     def get(self, request):
#         buildings = NewBuilding.objects.all()
#         serializer = NewBuildingSerializer(buildings,many=True)
#         print("Data: ",serializer.data)
#         print("Type of data: ", type(serializer.data))
#         print("Serializer: ", serializer)
#         return Response({"buildings": serializer.data})

class MicroDistrictChoices(APIView):
    def get(self,request):
        micro_district_choices = {}
        micro_district_choices['default'] = choices.MICRO_DISTRICT_DEFAULT_CHOICE + choices.MICRO_DISTRICT_DOES_NOT_EXIST_CHOICE
        micro_district_choices['saltovka'] = choices.MICRO_DISTRICT_SALTOVKA_CHOICES
        micro_district_choices['severnaya_saltovka'] = choices.MICRO_DISTRICT_SEVERNAYA_SALTOVKA_CHOICES
        json_choices = json.dumps(micro_district_choices, ensure_ascii=False)
        db_values = {'saltovka_dbvalue' : choices.SALTOVKA, 'severnaya_saltovka_dbvalue': choices.SEVERNAYA_SALTOVKA}
        return JsonResponse({'micro_district_choices':micro_district_choices, 'db_values':db_values})

class FindBuildings(APIView):
    def get(self,request):
        buildings = NewBuilding.objects.all()
        name_contains_query = request.GET.get('name_contains')
        address_contains_query = request.GET.get('address_contains')
        district_contains_query = request.GET.get('district_contains-select')
        developer_contains_query = request.GET.get('developer_contains-select')

        if name_contains_query != '' and name_contains_query is not None:
            buildings = buildings.filter(name__icontains=name_contains_query)
        else:
            name_contains_query = ''
        if address_contains_query != '' and address_contains_query is not None:
            buildings &= buildings.filter(address__icontains=address_contains_query)
        else:
            address_contains_query = ''
        if district_contains_query != '' and district_contains_query is not None and district_contains_query != choices.NOT_COMPLETED:
            buildings &= buildings.filter(
                district__icontains=district_contains_query)
        else:
            district_contains_query = ''
        if developer_contains_query != '' and developer_contains_query is not None:
            buildings &= buildings.filter(developer__icontains=developer_contains_query)
        else:
            developer_contains_query = ''

        serializer = NewBuildingSerializer(buildings,many=True)

        return Response({'buildings':serializer.data})



class AddressChecker(APIView):
    def get(self,request):
        print("Ajax request is accepted")
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
                    administrative_district_id = District.objects.get(dist_ukr=pure_district).id
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
