from django.shortcuts import render

# Create your views here.
def map(request):
  return render(request, 'park/map.html', {})

def add_spot(request):
  """
    View to add a new spot to upspot.
  """
  return redirect('/')

def add_vehicle(request):
  """
    View to add a new vehicle to upspot.
  """
  return redirect('/')

def reserve_spot(request):
  """
    View to handle booking a spot.
  """

def 
