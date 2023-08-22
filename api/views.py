from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MealSerializer ,RatingSerializer
from .models import Meal ,Rating

# Create your views here.

class Meal_viewSet(viewsets.ModelViewSet):
    queryset= Meal.objects.all()
    serializer_class= MealSerializer


class Rating_viewSet(viewsets.ModelViewSet):
    queryset= Rating.objects.all()
    serializer_class= RatingSerializer