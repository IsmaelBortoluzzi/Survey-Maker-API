from django.contrib.auth.models import User
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=64, default='')
    population = models.IntegerField()


class State(models.Model):
    name = models.CharField(max_length=64, default='')
    population = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)


class City(models.Model):
    name = models.CharField(max_length=64, default='')
    population = models.IntegerField()
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    is_author = models.BooleanField(default=False)
    gender = models.CharField(max_length=16, default='')
    birthday = models.DateField()
