# from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NewBuilding
from .serializers import NewBuildingSerializer

class NewBuildingView(APIView):
    def get(self, request):
        buildings = NewBuilding.objects.all()
        serializer = NewBuildingSerializer(buildings,many=True)
        # print(serializer)
        return Response({"buildings": serializer.data})

    def post(self, request):
        building = request.data.get('building')
        print(building)
        # Create an article from the above data
        serializer = NewBuildingSerializer(data=building)
        if serializer.is_valid(raise_exception=True):
            building_saved = serializer.save()
        return Response({"success": "building '{}' created successfully".format(building_saved.name)})
