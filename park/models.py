from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class Spot(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  address = models.CharField(max_length=100)
  available = models.BooleanField(default=True)
  in_use = models.BooleanField(default=False)
  location = models.PointField()
  rating = models.IntegerField(default=0)
  num_ratings = models.IntegerField(default=0)
  num_reservations = models.IntegerField(default=0)

  def shorthand_address(self):
    """
      Returns street address from address.
      Ex. 841 E Meda, Glendora, CA, US ---> 841 E Meda
    """
    return self.address.split(",")[0]

  def walking_time(self):
    """
      Returns an estimated walking time in minutes from a distance.
      TODO: Add a try catch because distance is an annotated value.
    """
    return int(self.distance.m // 83)

class Vehicle(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  make = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  license_plate = models.CharField(max_length=20, default="XXXXXXX")

class Reservation(models.Model):
  spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
  price = models.IntegerField()
  buyer = models.ForeignKey(User, related_name="buyer_user")
  seller = models.ForeignKey(User, related_name="seller_user")
  start = models.DateTimeField(blank=True)
  end = models.DateTimeField(blank=True, null=True)

class BuyerProfile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=35)
  phone_number = models.CharField(max_length=20)
  rating = models.IntegerField(default=0)
  num_ratings = models.IntegerField(default=0)
  num_reservations = models.IntegerField(default=0)

class SellerProfile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=35)
  phone_number = models.CharField(max_length=20)
  rating = models.IntegerField(default=0)
  num_ratings = models.IntegerField(default=0)
  num_reservations = models.IntegerField(default=0)
  stripe_id = models.CharField(max_length=50)


class GeoBucket(models.Model):
  ''' Spot availability hours assumptions
    1.  Get user location
        as location -> spot, price increases
        Use case: Booking from home vs booking from outside

    2.  Surge multiplier is a constant multiplied to the price
        Surge based on spots available/existing
  '''
  geohash = models.CharField(max_length=50)
  spots = models.IntegerField(default=0)
  reservations = models.IntegerField(default=0)
  searches = models.IntegerField(default=0)
  price = models.IntegerField(default=500)
  
  def search(self):
    self.searches += 1

  def spot(self):
    self.spots += 1

  def calc_price(self):
    fixed_price = 5
    ratio = self.searches / float(self.spots)
    surge = (self.reservations * ratio) / 100 + 1
    return fixed_price * surge
