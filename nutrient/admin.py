from django.contrib import admin
from .models import Crop , Nutrient , Element
# Register your models here.

class CropAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ElementAdmin(admin.ModelAdmin):
    list_display = ('name',)

class NutrientAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Crop , CropAdmin) 
admin.site.register(Element , ElementAdmin) 
admin.site.register(Nutrient , CropAdmin) 