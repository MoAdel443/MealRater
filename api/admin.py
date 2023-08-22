from django.contrib import admin
from .models import Rating,Meal

# Register your models here.

class MealAdmin(admin.ModelAdmin):
    list_display=['id','title','description']
    search_fields=['title','description']
    list_filter=['title','description']

class RatingAdmin(admin.ModelAdmin):
    list_display=['id','user','meal','stars']
    list_filter=['meal','user']


admin.site.register(Meal ,MealAdmin)
admin.site.register(Rating ,RatingAdmin)
