from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MealSerializer ,RatingSerializer ,UserSerializer
from .models import Meal ,Rating
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny ,IsAdminUser ,IsAuthenticated ,IsAuthenticatedOrReadOnly


# Create your views here.

class User_viewset(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class= UserSerializer

    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid()
        self.perform_create(serializer)
        token , created = Token.objects.get_or_create(user=serializer.instance)

        return Response(
            {
                "token":token.key
            },
            status=status.HTTP_201_CREATED
        )
    
    def list(self, request, *args, **kwargs):
        responce={'message':'you cant create rating like that'}

        return Response(responce,status=status.HTTP_400_BAD_REQUEST) 
 

class Meal_viewSet(viewsets.ModelViewSet):
    queryset= Meal.objects.all()
    serializer_class= MealSerializer

    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

    @action(detail=True,methods=['post'])
    def rate_meal(self,request,pk):
        if 'stars' in request.data:
            # username= request.data['username']
            meal=Meal.objects.get(id=pk)
            stars=request.data['stars']
            user = request.user
            # user=User.objects.get(username=username)
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

    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)