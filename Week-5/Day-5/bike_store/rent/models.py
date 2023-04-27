from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    COUNTRY_CHOICES = [
        ('IL', 'Israel'),
        ('US', 'United States'),
        ('CA', 'Canada'),
    ]
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES)

    def __str__(self) -> str:
        return f'{self.first_name}, {self.last_name}, {self.email}, {self.phone_number}, {self.address}, {self.city}, {self.country}'



class Vehicle_Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'


class Vehicle_Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'


class Vehicle(models.Model):
    vehicle_type =  models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    real_cost =  models.FloatField()
    size = models.ForeignKey(Vehicle_Size, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.vehicle_type}, {self.date_created}, {self.real_cost}, {self.size}'


class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def clean(self):
        if self.rental_date > self.return_date:
            raise ValidationError('Rental date cannot be later than return date.')
        now = timezone.now()
        if self.rental_date > now or self.return_date > now:
            raise ValidationError('Rental and return dates cannot be later than current date.')
    
    def __str__(self) -> str:
        return f'{self.rental_date}, {self.return_date}, {self.customer_id}, {self.vehicle}'
        


class Rental_Rate(models.Model):
    daily_rate = models.FloatField()
    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(Vehicle_Size, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.daily_rate}, {self.vehicle_type}, {self.vehicle_size}'