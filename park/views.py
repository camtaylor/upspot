from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import  D
from models import Spot, Vehicle, GeoBucket
from django.contrib.gis.db.models.functions import Distance
from scripts import geohash_encode, geohash_decode


def map(request):
  """
    View to handle spot map and search.
  """
  if request.method == 'GET':
    radius = request.GET.get("radius")
    if not radius:
      radius = 5
    if request.GET.get("lat") and request.GET.get("lng"):
      lattitude =  float(request.GET.get("lat"))
      longitude = float(request.GET.get("lng"))
      search_point = Point(longitude, lattitude)
      # Find geohash to get grid value and retrieve geobucket.
      spot_geohash = geohash_encode(lattitude, longitude)[:6]
      geobucket, created = GeoBucket.objects.get_or_create(geohash=spot_geohash)
      # Add a search to the given geobucket and save.
      geobucket.search()
      geobucket.save()
      #Get all spots within radius from search point.
      spots = Spot.objects.filter(
      location__distance_lte=(search_point, D(mi=radius))).annotate(
      distance=Distance('location', search_point)).order_by(
      'distance')
    else:
      spots = []
    search = request.GET.get("search", "")
  return render(request, 'park/map.html', {"search" : search, "spots" : spots, "radius" : radius})

def add_spot(request):
  """
    View to add a new spot to upspot.
  """
  if request.method == 'GET':
    spots = Spot.objects.filter(owner=request.user)
    return render(request, 'park/spot.html', {'spots' : spots})
  elif request.method =='POST':
    owner = request.user
    lattitude = float(request.POST.get("lat"))
    longitude = float(request.POST.get("lng"))
    address = request.POST.get("address")
    new_spot = Spot()
    new_spot.owner = owner
    new_spot.location = Point(longitude, lattitude)
    new_spot.address = address
    new_spot.save()
    return redirect('/park/spots')

def add_vehicle(request):
  """
    View to add a new vehicle to upspot.
  """
  if request.method == 'GET':
    vehicles = Vehicle.objects.filter(owner=request.user)
    return render(request, 'park/vehicle.html', {'vehicles' : vehicles})
  elif request.method =='POST':
    owner = request.user
    make = request.POST.get("make")
    model = request.POST.get("model")
    new_vehicle = Vehicle()
    new_vehicle.owner = owner
    new_vehicle.make = make
    new_vehicle.model = model
    new_vehicle.save()
    return redirect('/park/vehicles')

def reserve_spot(request):
  """
    View to handle booking a spot.
  """
  if request.method == 'GET':
    spot_id = request.GET.get("id")
    if spot_id:
      spot = Spot.objects.get(pk=spot_id)
    else:
      spot = None
    return render(request, 'park/reserve.html', {'spot' : spot})
  elif request.method == 'POST':
    return render(request, 'park/reserve.html', {})
  else:
    return redirect('/')

def manage_reservations(request):
  """
     View to check in and check out of spots
  """
