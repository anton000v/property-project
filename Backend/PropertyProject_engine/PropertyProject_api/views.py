# from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NewBuilding
from .serializers import NewBuildingSerializer
from . import choices
from django.http import JsonResponse, HttpResponse, Http404
from .utils import Houses
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

def json_response(something):
    return HttpResponse(
        json.dumps(something),
        content_type = 'application/javascript; charset=utf8'
    )

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


class AddressChecker(APIView):
    def get(self,request):
        print("Ajax request is accepted")
        if request.is_ajax():
            street = request.GET.get('street', None)
            house_number = request.GET.get('house_number', None)
            houses = Houses(street=street, house_number=house_number)
            if houses.is_house_exist():
                houses.fill_all_letters()
                response = {
                'without_letter': choices.WITHOUT_LETTER ,
                'without_letter_for_humans':choices.WITHOUT_LETTER_FOR_HUMANS,
                'houses': houses.house_letters
                }
                return JsonResponse(response)
            else:
                response = JsonResponse({"error": '"{}, {}" не найдено в Харькове'.format(street,house_number)})
                response.status_code = 403 # To announce that the user isn't allowed to publish
                return response
        else:
            raise Http404
#
# class UpdateHouseLetterValidChoices(APIView):
#     def post(self,request):
