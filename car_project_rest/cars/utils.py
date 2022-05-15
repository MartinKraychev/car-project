from car_project_rest.cars.models import CarBrand, CarModel


def make_data(data):
    car_brand_data = data.pop('car_brand')
    car_brand_name = car_brand_data['name']

    car_model_data = data.pop('car_model')
    car_model_name = car_model_data['name']

    # If Brand exists - retrieve it
    car_brand = CarBrand.objects.filter(name=car_brand_name).first()

    # If brand doesn't exist- create it
    if not car_brand:
        car_brand = CarBrand.objects.create(name=car_brand_name)

    data['car_brand'] = car_brand

    car_model = CarModel.objects.filter(name=car_model_name).first()
    if not car_model:
        car_model = CarModel.objects.create(name=car_model_name, car_brand=car_brand)

    data['car_model'] = car_model
    return data
