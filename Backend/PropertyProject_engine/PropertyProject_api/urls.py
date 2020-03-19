from django.urls import path
from django.contrib import admin
from . import views
app_name = "property project"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('api/buildings/', views.NewBuildingView.as_view()),
    path('api/get-micro-districts/', views.GetMicroDistrictChoices.as_view()),
    ]
