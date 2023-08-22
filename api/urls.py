from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Meal_viewSet ,Rating_viewSet

router=DefaultRouter()
router.register('meal',Meal_viewSet)
router.register('rating',Rating_viewSet)



urlpatterns = [
    path('', include(router.urls)),
]
