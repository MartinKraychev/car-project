from django.contrib.auth import get_user_model
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from car_project_rest.cars.models import CarBrand, CarModel, UserCar

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username',)


class CarBrandSerializer(ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ('id', 'name',)


class CarModelSerializer(ModelSerializer):
    car_brand = PrimaryKeyRelatedField(queryset=CarBrand.objects.all(), allow_null=False, required=True)

    class Meta:
        model = CarModel
        fields = ('id', 'name', 'car_brand')


class CarModelListRetrieveSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'name', 'car_brand')


class UserCarPutCreateSerializer(ModelSerializer):
    car_model = PrimaryKeyRelatedField(queryset=CarModel.objects.all(), allow_null=False, required=True)

    # adds the user to the serializer
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = UserCar
        fields = ('id', 'first_reg', 'odometer', 'car_model')


class UserCarListRetrieveSerializer(ModelSerializer):
    car_model = CarModelListRetrieveSerializer(many=False, )
    user = UserSerializer(many=False, )

    class Meta:
        model = UserCar
        fields = ('id', 'first_reg', 'odometer', 'car_model', 'user')
