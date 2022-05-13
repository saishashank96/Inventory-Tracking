from django.db import models

# Create your models here.
class Inventory(models.Model):
    Name = models.CharField(max_length=200)
    Quantity = models.IntegerField(default=0)
class deleted(models.Model):
    Name = models.CharField(max_length=200)
    Quantity = models.IntegerField(default=0)
    Comment = models.CharField(max_length=200)