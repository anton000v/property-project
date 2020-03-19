# from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NewBuilding
from .serializers import NewBuildingSerializer
from . import choices
from django.http import JsonResponse, HttpResponse
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

class GetMicroDistrictChoices(APIView):
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
    # def post(self, request):
    #     building = request.data.get('building')
    #     print(building)
    #     # Create an article from the above data
    #     serializer = NewBuildingSerializer(data=building)
    #     if serializer.is_valid(raise_exception=True):
    #         building_saved = serializer.save()
    #     return Response({"success": "building '{}' created successfully".format(building_saved.name)})
