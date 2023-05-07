from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.first_name, self.last_name}'


class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    created_in_country = models.ForeignKey("Country", on_delete=models.PROTECT)
    available_in_countries = models.ManyToManyField("Country", related_name="films")
    category = models.ManyToManyField("Category", related_name='films')
    director = models.ManyToManyField("Director", related_name='films')

    def __str__(self) -> str:
        return f"{self.title}"

