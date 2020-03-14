from django.urls import path
from django.contrib import admin
from .views import NewBuildingView
app_name = "property project"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('buildings/', NewBuildingView.as_view()),
    ]
