# car-project

To test locally:
 - Create venv
 - Install dependencies


API Calls:

Auth:
    
 - register : POST http://127.0.0.1:8000/auth/register/
 - login: POST http://127.0.0.1:8000/auth/login/
   

 Cars:
    
- brands:

    - GET http://127.0.0.1:8000/cars/brands/
    - GET http://127.0.0.1:8000/cars/brands/{id}
    - POST http://127.0.0.1:8000/cars/brands/
    - PUT/PATCH http://127.0.0.1:8000/cars/brands/{id}
    - DELETE http://127.0.0.1:8000/cars/brands/{id}

- soft deleted brands:
    
    - GET http://127.0.0.1:8000/cars/deleted%20brands/
    - GET http://127.0.0.1:8000/cars/deleted%20brands/{id}
    - PUT http://127.0.0.1:8000/cars/deleted%20brands/{id} - restores the instance
    - DELETE http://127.0.0.1:8000/cars/deleted%20brands/{id} - hard delete

- models:

    - GET http://127.0.0.1:8000/cars/models/
    - GET http://127.0.0.1:8000/cars/models/{id}
    - POST http://127.0.0.1:8000/cars/models/
    - PUT/PATCH http://127.0.0.1:8000/cars/models/{id}
    - DELETE http://127.0.0.1:8000/cars/models/{id}

- User cars:

    - GET http://127.0.0.1:8000/cars/user-car/
    - GET http://127.0.0.1:8000/cars/user-car/{id}
    - POST http://127.0.0.1:8000/cars/user-car/
    - PUT/PATCH http://127.0.0.1:8000/cars/user-car/{id}
    - DELETE http://127.0.0.1:8000/cars/user-car/{id}


Filters:

- Car brand by name - GET http://127.0.0.1:8000/cars/brands/?name={name}
- Car model by name - - GET http://127.0.0.1:8000/cars/models/?name={name}
- User car by first reg - GET http://127.0.0.1:8000/cars/user-car/?first_reg={first_reg}
