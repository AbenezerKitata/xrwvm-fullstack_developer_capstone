# server/djangoapp/models.py
# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    founded_year = models.IntegerField(
        null=True, 
        blank=True,
        validators=[MinValueValidator(1800), MaxValueValidator(2023)]
    )
    country = models.CharField(max_length=50, blank=True)
    
    # Any other fields you would like to include in car make model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # __str__ method to print a car make object
    def __str__(self):
        return self.name


# Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    # Many-To-One relationship to Car Make model
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    
    # Name
    name = models.CharField(max_length=100)
    
    # Type with choices
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('HATCHBACK', 'Hatchback'),
        ('TRUCK', 'Truck'),
        ('VAN', 'Van'),
    ]
    type = models.CharField(max_length=20, choices=CAR_TYPES, default='SUV')
    
    # Year with validators
    year = models.IntegerField(
        default=2023,
        validators=[MinValueValidator(2015), MaxValueValidator(2023)]
    )
    
    # Any other fields you would like to include in car model
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    engine_size = models.CharField(max_length=20, blank=True)
    fuel_type = models.CharField(max_length=20, blank=True)
    transmission = models.CharField(max_length=20, blank=True)
    color = models.CharField(max_length=30, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # __str__ method to print a car model object
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"