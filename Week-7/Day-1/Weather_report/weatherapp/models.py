from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

CHOICES = (
                ('sunny', 'Sunny'),
                ('cloudy', 'Cloudy'),
                ('windy', 'Windy'),
                ('rainy', 'Rainy'),
                ('stormy', 'Stormy')
                )

class Report(models.Model):

    location = models.CharField(max_length=100)
    temperature = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(60.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    weather_type = models.CharField(max_length=20, choices=CHOICES)

    def __str__(self):
        return f'{self.location}, {self.temperature}'