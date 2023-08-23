from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MealSerializer ,RatingSerializer
from .models import Meal ,Rating
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
# Create your views here.

class Meal_viewSet(viewsets.ModelViewSet):
    queryset= Meal.objects.all()
    serializer_class= MealSerializer

    @action(detail=True,methods=['post'])
    def rate_meal(self,request,pk):
        if 'stars' in request.data:
            username= request.data['username']
            meal=Meal.objects.get(id=pk)
            stars=request.data['stars']
            user=User.objects.get(username=username)
            try:
                #update
                rating=Rating.objects.get(meal=meal.pk,user=user.pk)
                rating.stars=stars
                rating.save()
                serializer = RatingSerializer(rating,many=False)
                json={
                    'message':'data Updated Successfully',
                    'restul':serializer.data
                }
                return Response(json,status=status.HTTP_200_OK)
            
            except:
                #create
                rating =Rating.objects.create(stars=stars,meal=meal,user=user)
                serializer = RatingSerializer(rating,many=False)
                json={
                    'message':'data Created Successfully',
                    'restul':serializer.data
                }
                return Response(json,status=status.HTTP_201_CREATED)
                
        else:
            json={
                'message':'Something Went Wrong!'
            }
            return Response(json,status=status.HTTP_400_BAD_REQUEST)


class Rating_viewSet(viewsets.ModelViewSet):
    queryset= Rating.objects.all()
    serializer_class= RatingSerializer