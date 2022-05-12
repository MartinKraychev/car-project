from django.urls import path, include
from rest_framework import routers

from car_project_rest.cars.views import CarBrandViewSet, CarModelViewSet, UserCarViewSet

from car_project_rest.cars.views import CarBrandDeletedViewSet

router = routers.DefaultRouter()


router.register(r'brands', CarBrandViewSet, 'car brands')
router.register(r'models', CarModelViewSet, 'car models')
router.register(r'user-car', UserCarViewSet, 'user cars')
router.register(r'deleted brands', CarBrandDeletedViewSet, 'deleted brands')

urlpatterns = (
    path('', include(router.urls)),
)
