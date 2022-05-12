from rest_framework import status, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from car_project_rest.cars.models import CarBrand, CarModel, UserCar
from car_project_rest.cars.serializers import CarBrandSerializer, CarModelSerializer, UserCarPutCreateSerializer, \
    UserCarListRetrieveSerializer


class CarBrandViewSet(ModelViewSet):
    serializer_class = CarBrandSerializer
    # Custom typed filter by name
    filterset_fields = ('name',)
    permission_classes = (
        IsAuthenticated,
    )

    def get_queryset(self):
        queryset = CarBrand.objects.all().order_by('id')

        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Executes soft delete for the instance and all the related items
    def perform_destroy(self, instance):
        related_models = CarModel.objects.filter(car_brand=instance)
        for model in related_models:
            model.soft_delete()
        instance.soft_delete()


class CarModelViewSet(ModelViewSet):
    serializer_class = CarModelSerializer
    # Custom typed filter by name
    filterset_fields = ('name',)
    permission_classes = (
        IsAuthenticated,
    )

    def get_queryset(self):
        queryset = CarModel.objects.all().order_by('id')

        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.soft_delete()


class UserCarViewSet(ModelViewSet):
    # Custom typed filter by first_reg
    filterset_fields = ('first_reg',)
    permission_classes = (
        IsAuthenticated,
    )

    def get_serializer_class(self):
        # Using different serializers depending on action

        if self.action == 'list' or self.action == 'retrieve':
            return UserCarListRetrieveSerializer
        else:
            return UserCarPutCreateSerializer

    def get_queryset(self):
        queryset = UserCar.objects.all().order_by('id')

        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.soft_delete()


class CarBrandDeletedViewSet(mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet,
                             mixins.UpdateModelMixin):
    serializer_class = CarBrandSerializer
    permission_classes = (
        IsAuthenticated,
    )
    """
    View that returns only deleted objects, using the update method restores the object
    """

    def get_queryset(self):
        queryset = CarBrand.deleted_objects.all().order_by('id')

        return queryset

    # Executes restore of the car brand and all related models

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.restore()
        related_models = CarModel.deleted_objects.filter(car_brand=instance)
        for model in related_models:
            model.restore()

        return Response('Item was restored')
