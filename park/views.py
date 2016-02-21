from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point
from models import Spot

# Create your views here.
def map(request):
  if request.method == 'GET':
    spots = Spot.objects.all()
    search = request.GET.get("search", "")
  return render(request, 'park/map.html', {"search" : search, "spots" : spots})

def add_spot(request):
  """
    View to add a new spot to upspot.
  """
  if request.method == 'GET':
    spots = Spot.objects.all()
    return render(request, 'park/spot.html', {'spots' : spots})
  elif request.method =='POST':
    lattitude = float(request.POST.get("lat"))
    longitude = float(request.POST.get("lng"))
    address = request.POST.get("address")
    new_spot = Spot()
    new_spot.location = Point(longitude, lattitude)
    new_spot.address = address
    new_spot.save()
    return redirect('/park/add')

def add_vehicle(request):
  """
    View to add a new vehicle to upspot.
  """
  return redirect('/')

def reserve_spot(request):
  """
    View to handle booking a spot.
  """
  return redirect('/')
