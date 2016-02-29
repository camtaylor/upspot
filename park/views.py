from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import  D
from models import Spot, Vehicle
from django.contrib.gis.db.models.functions import Distance

# Create your views here.
def map(request):
  if request.method == 'GET':
    radius = request.GET.get("radius")
    if not radius:
      radius = 5
    if request.GET.get("lat") and request.GET.get("lng"):
      lattitude =  float(request.GET.get("lat"))
      longitude = float(request.GET.get("lng"))
      search_point = Point(longitude, lattitude)

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
    vehicles = Vehicle.objects.all()
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
    return render(request, 'park/reserve.html', {})
  elif request.method == 'POST':
    return render(request, 'park/reserve.html', {})
  else:
    return redirect('/')
