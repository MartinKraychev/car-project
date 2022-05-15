from django.contrib.auth import get_user_model
from django.db import models

from car_project_rest.accounts.models import SoftDeleteModel

UserModel = get_user_model()


class CarBrand(SoftDeleteModel):
    CAR_BRAND_NAME_MAX_LENGTH = 20

    name = models.CharField(
        max_length=CAR_BRAND_NAME_MAX_LENGTH,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class CarModel(SoftDeleteModel):
    CAR_MODEL_NAME_MAX_LENGTH = 20

    name = models.CharField(
        max_length=CAR_MODEL_NAME_MAX_LENGTH,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    car_brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.name}'


class UserCar(SoftDeleteModel):
    first_reg = models.DateField()

    odometer = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    car_model = models.ForeignKey(
        CarModel,
        on_delete=models.CASCADE
    )

    car_brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.user} {self.car_model}'

