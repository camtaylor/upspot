from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class Spot(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  address = models.CharField(max_length=100)
  available = models.BooleanField(default=False)
  location = models.PointField()
  rating = models.IntegerField(default=0)
  num_ratings = models.IntegerField(default=0)
  num_reservations = models.IntegerField(default=0)

class Vehicle(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  make = models.CharField(max_length=50)
  model = models.CharField(max_length=50)

class Reservation(models.Model):
  spot = models.ForeignKey(Spot)
  price = models.IntegerField()
  buyer = models.ForeignKey(User, related_name="buyer_user")
  seller = models.ForeignKey(User, related_name="seller_user")
  start = models.DateTimeField(blank=True)
  end = models.DateTimeField(blank=True)

class BuyerProfile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=35)
  phone_number = models.CharField(max_length=20)
  rating = models.IntegerField(default=0)
  num_ratings = models.IntegerField(default=0)
  num_reservations = models.IntegerField(default=0)
