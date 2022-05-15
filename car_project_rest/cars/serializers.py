from django.contrib.auth import get_user_model
from rest_framework import serializers

from car_project_rest.cars.models import CarBrand, CarModel, UserCar
from car_project_rest.cars.utils import make_data

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username',)


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ('id', 'name',)


class CarModelForUserCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ('id', 'name',)


class CarModelSerializer(serializers.ModelSerializer):
    car_brand = CarBrandSerializer(many=False, )

    def create(self, validated_data):
        car_brand_data = validated_data.pop('car_brand')
        car_brand_name = car_brand_data['name']
        name = validated_data.pop('name')

        # If Brand exists - retrieve it
        car_brand = CarBrand.objects.filter(name=car_brand_name).first()

        # If brand doesn't exist- create it
        if not car_brand:
            car_brand = CarBrand.objects.create(name=car_brand_name)

        # Creates the model with either new or existing brand
        car_model = CarModel.objects.create(name=name, car_brand=car_brand)

        return car_model

    def update(self, instance, validated_data):
        car_brand_data = validated_data.pop('car_brand')
        car_brand_name = car_brand_data['name']
        name = validated_data.pop('name')

        # If Brand exists - retrieve it
        car_brand = CarBrand.objects.filter(name=car_brand_name).first()

        # If brand doesn't exist- create it
        if not car_brand:
            car_brand = CarBrand.objects.create(name=car_brand_name)

        # Updates the model with either new or existing brand
        instance.name = name
        instance.car_brand = car_brand
        instance.save()

        return instance

    class Meta:
        model = CarModel
        fields = ('id', 'name', 'car_brand')


class CarModelListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'name', 'car_brand')


class UserCarCreatePutDeleteSerializer(serializers.ModelSerializer):
    car_model = CarModelForUserCarSerializer(many=False, )
    car_brand = CarBrandSerializer(many=False, )

    def create(self, validated_data):
        # # adds the user from the request to the serializer
        validated_data['user'] = self.context['request'].user

        validated_data = make_data(validated_data)
        car_brand = validated_data.pop('car_brand')
        car_model = validated_data.pop('car_model')
        # Creates and returns the instance
        car_instance = UserCar.objects.create(car_brand=car_brand, car_model=car_model, **validated_data)

        return car_instance

    def update(self, instance, validated_data):
        validated_data = make_data(validated_data)

        instance.first_reg = validated_data.pop('first_reg')
        instance.odometer = validated_data.pop('odometer')
        instance.car_brand = validated_data.pop('car_brand')
        instance.car_model = validated_data.pop('car_model')
        instance.save()

        return instance

    class Meta:
        model = UserCar
        fields = ('id', 'first_reg', 'odometer', 'car_model', 'car_brand')


class UserCarListRetrieveSerializer(serializers.ModelSerializer):
    car_model = CarModelListRetrieveSerializer(many=False, )
    car_brand = CarBrandSerializer(many=False, )
    user = UserSerializer(many=False, )

    class Meta:
        model = UserCar
        fields = ('id', 'first_reg', 'odometer', 'car_model', 'car_brand', 'user')
