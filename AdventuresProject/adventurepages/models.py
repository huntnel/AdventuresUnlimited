from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Hike(models.Model):
    hikename = models.CharField(max_length=50)
    elevationgain = models.IntegerField(default=0)
    length = models.FloatField(default=0.0)
    description = models.CharField(max_length=250)
    bathroom = models.BooleanField(default=True)
    potablewater = models.BooleanField(default=True)
    # firepits = models.BooleanField
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zipcode = IntegerField(default=0)
    difficulty = models.CharField(max_length=10)
    class Meta :
        db_table = "hiking"

    def __str__(self) :
        return (self.hikename)

class Camp(models.Model):
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