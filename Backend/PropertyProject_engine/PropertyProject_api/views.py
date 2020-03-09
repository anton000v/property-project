# from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NewBuilding
from .serializers import NewBuildingSerializer

class NewBuildingView(APIView):
    def get(self, request):
        buildings = NewBuilding.objects.all()
        serializer = NewBuildingSerializer(buildings,many=True)
        print(serializer)
        return Response({"buildings": serializer.data})
