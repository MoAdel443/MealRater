from rest_framework import serializers
from .models import Rating,Meal
from django.contrib.auth.models import User

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields =['id','title','description','no_of_ratings','avg_rating']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields =['id','user','meal','stars']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id','username','password']
