from django.db import models

# Create your models here.

class Cleaner(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    quality_score = models.ForeignKey(Customer, on_delete=models.CASCADE)

class City(models.Model):
    city = models.CharField(max_length=200)
    check = models.BooleanField

class Customer(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone = models.IntegerField
    quality_score = models.FloatField