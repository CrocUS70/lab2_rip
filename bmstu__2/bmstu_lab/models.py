from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)

class Book1(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)

class Company(models.Model):
    name_company = models.CharField(max_length=30)
    product = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Views_product(models.Model):
    name_product = models.CharField(max_length=30)
    price = models.CharField(max_length=255)
    description = models.CharField(max_length=255)