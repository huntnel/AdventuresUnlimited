from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Hiking(models.Model):
    hikename = models.CharField(max_length=50)
    elevationgain = models.IntegerField
    length = models.FloatField
    description = models.CharField(max_length=250)
    bathroom = models.BooleanField
    potablewater = models.BooleanField
    firepits = models.BooleanField
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zipcode = IntegerField
    difficulty = models.CharField(max_length=10)
    class Meta :
        db_table = "hiking"

    def __str__(self) :
        return (self.hikename)

class Camping(models.Model):
    campname = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.FloatField
    bathroom = models.BooleanField
    potablewater = models.BooleanField
    firepits = models.BooleanField
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zipcode = IntegerField

    class Meta :
        db_table = "camping"

    def __str__(self) :
        return (self.campname)