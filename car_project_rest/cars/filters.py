from django_filters import FilterSet, ModelChoiceFilter

from car_project_rest.cars.models import CarBrand, CarModel, UserCar


class ModelFilter(FilterSet):
    car_brand = ModelChoiceFilter(queryset=CarBrand.objects.all())

    class Meta:
        model = CarModel
        fields = ['car_brand__name', 'name']


class UserCarFilter(FilterSet):
    car_brand = ModelChoiceFilter(queryset=CarBrand.objects.all())
    car_model = ModelChoiceFilter(queryset=CarModel.objects.all())

    class Meta:
        model = UserCar
        fields = ['car_model__name', 'car_brand__name', 'odometer', 'first_reg']
