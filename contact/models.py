from django.contrib.auth.models import User
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=64, default='')
    population = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.name}'


class State(models.Model):
    name = models.CharField(max_length=64, default='')
    population = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    acronym = models.CharField(max_length=16, default='')

    def __str__(self):
        return f'{self.id} - {self.name} - {self.acronym}'


class City(models.Model):
    name = models.CharField(max_length=64, default='')
    population = models.IntegerField()
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.state.acronym}'


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    is_author = models.BooleanField(default=False)
    gender = models.CharField(max_length=16, default='')
    birthday = models.DateField()

    def __str__(self):
        return f'{self.id} - {self.user.first_name} {self.user.last_name}'
