from django.contrib import admin
from django.contrib.admin import ModelAdmin


from car_project_rest.accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    list_display = ['username', 'gender', 'date_of_birth', 'is_staff', 'is_superuser']


