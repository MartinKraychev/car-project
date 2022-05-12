from django.contrib import admin
from django.contrib.admin import ModelAdmin

from car_project_rest.cars.models import CarBrand, CarModel, UserCar


@admin.register(CarBrand)
class CarBrandAdmin(ModelAdmin):
    list_display = ['name',]


@admin.register(CarModel)
class CarModelAdmin(ModelAdmin):
    list_display = ['name', 'car_brand']


@admin.register(UserCar)
class UserCarAdmin(ModelAdmin):
    list_display = ['first_reg', 'odometer', 'car_model']
