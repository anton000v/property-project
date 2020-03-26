# from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NewBuilding, District
from .serializers import NewBuildingSerializer
from . import choices
from django.http import JsonResponse, HttpResponse, Http404
from .utils import House
import json

class NewBuildingView(APIView):
    def get(self, request):
        buildings = NewBuilding.objects.all()
        serializer = NewBuildingSerializer(buildings,many=True)
        # print(serializer)
        print("Data: ",serializer.data)
        print("Type of data: ", type(serializer.data))
        print("Serializer: ", serializer)
        return Response({"buildings": serializer.data})

# def json_response(something):
#     return HttpResponse(
#         json.dumps(something),
#         content_type = 'application/javascript; charset=utf8'
#     )

class MicroDistrictChoices(APIView):
    def get(self,request):
        # district_choices = json.dumps(FULL_MICRO_DISTRICT_CHOICES,ensure_ascii=False)
        micro_district_choices = {}
        micro_district_choices['default'] = choices.MICRO_DISTRICT_DEFAULT_CHOICE + choices.MICRO_DISTRICT_DOES_NOT_EXIST_CHOICE
        micro_district_choices['saltovka'] = choices.MICRO_DISTRICT_SALTOVKA_CHOICES
        micro_district_choices['severnaya_saltovka'] = choices.MICRO_DISTRICT_SEVERNAYA_SALTOVKA_CHOICES
        # json_choices = {}
        json_choices = json.dumps(micro_district_choices, ensure_ascii=False)

        db_values = {'saltovka_dbvalue' : choices.SALTOVKA, 'severnaya_saltovka_dbvalue': choices.SEVERNAYA_SALTOVKA}
        # json_choices = {"json":micro_district_choices}
        # serializer = MySerializer(json_choices,many=True)
        # print('choices: ',json_choices);
        # return Response({"micro_district_choices": serializer.data})
        # return HttpResponse(
        #     json.dumps(json_choices),
        #     content_type = 'application/javascript; charset=utf8'
        # )
        return JsonResponse({'micro_district_choices':micro_district_choices, 'db_values':db_values})

#-------------------- VERSION FOR LETTERS HELP
# class AddressChecker(APIView):
#     def get(self,request):
#         print("Ajax request is accepted")
#         if request.is_ajax():
#             street = request.GET.get('street', None)
#             house_number = request.GET.get('house_number', None)
#             houses = Houses(street=street, house_number=house_number)
#             if houses.is_house_exist():
#                 houses.fill_all_letters()
#                 response = {
#                 'without_letter': choices.WITHOUT_LETTER ,
#                 'without_letter_for_humans':choices.WITHOUT_LETTER_FOR_HUMANS,
#                 'houses': houses.house_letters
#                 }
#                 return JsonResponse(response)
#             else:
#                 response = JsonResponse({"error": '"{}, {}" не найдено в Харькове'.format(street,house_number)})
#                 response.status_code = 403 # To announce that the user isn't allowed to publish
#                 return response
#         else:
#             raise Http404

#-------------------- VERSION FOR LETTER CHECK
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
                # houses.fill_all_letters()
                    house.fill_district()
                    house.fill_location()
                    # print('DISTRICT  --->  ', house.house_district)
                    pure_district = house.house_district.split()[0]
                    administrative_district_id = District.objects.get(dist_ukr=pure_district).id
                    # print(house.lat,house.lng)
                    # print(' ID ---> ', administrative_district_id)
                    response = {
                    # 'without_letter': choices.WITHOUT_LETTER ,
                    # 'without_letter_for_humans':choices.WITHOUT_LETTER_FOR_HUMANS,
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
                        # "choices": choices.HOUSE_LETTER_CHOICES
                                                                  })
                    response.status_code = 403 # To announce that the user isn't allowed to publish
                    return response
        else:
            raise Http404
#
# class UpdateHouseLetterValidChoices(APIView):
#     def post(self,request):
