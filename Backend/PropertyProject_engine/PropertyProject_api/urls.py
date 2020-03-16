from django.urls import path
from django.contrib import admin
from .views import NewBuildingView, GetMicroDistricts
app_name = "property project"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('api/buildings/', NewBuildingView.as_view()),
    path('api/get_micro_districts/', GetMicroDistricts.as_view()),
    ]
