# server/djangoapp/populate.py
from .models import CarMake, CarModel

def initiate():
    # First, clear any existing data (optional)
    CarModel.objects.all().delete()
    CarMake.objects.all().delete()
    
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology"},
        {"name":"Mercedes", "description":"Great cars. German technology"},
        {"name":"Audi", "description":"Great cars. German technology"},
        {"name":"Kia", "description":"Great cars. Korean technology"},
        {"name":"Toyota", "description":"Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data["name"], description=data['description']))

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {"name":"Pathfinder", "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
        {"name":"Qashqai", "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
        {"name":"X-TRAIL", "type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
        {"name":"A-class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
        {"name":"C-class", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[1]},
        {"name":"E-class", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[1]},
        {"name":"A4", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[2]},
        {"name":"A5", "type":"COUPE", "year": 2023, "car_make":car_make_instances[2]},
        {"name":"A6", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[2]},
        {"name":"Sorento", "type":"SUV", "year": 2023, "car_make":car_make_instances[3]},
        {"name":"Carnival", "type":"VAN", "year": 2023, "car_make":car_make_instances[3]},
        {"name":"Cerato", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[3]},
        {"name":"Corolla", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[4]},
        {"name":"Camry", "type":"SEDAN", "year": 2023, "car_make":car_make_instances[4]},
        {"name":"Kluger", "type":"SUV", "year": 2023, "car_make":car_make_instances[4]},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'], 
            car_make=data['car_make'], 
            type=data['type'], 
            year=data['year']
        )
    
    print("Database populated with 5 car makes and 15 car models")