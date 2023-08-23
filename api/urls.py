from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Meal_viewSet ,Rating_viewSet ,User_viewset

router=DefaultRouter()
router.register('meal',Meal_viewSet)
router.register('rating',Rating_viewSet)
router.register('user',User_viewset)




urlpatterns = [
    path('', include(router.urls)),
]
