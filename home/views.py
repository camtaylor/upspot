from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
  user = request.user
  if user and user.is_active:
    return redirect('/park')
  return render(request, 'home/home.html', {})

def user_signup(request):
  if request.POST:
    user_email = request.POST.get("email", None)
    user_password = request.POST.get("password", None)
    if user_email and user_password:
      new_user = User.objects.create_user(username=user_email, email=user_email, password=user_password)
      user = authenticate(username=user_email, password=user_password)
      if user:
        login(request,user)
        return redirect('/park')
      else:
        return redirect('/')

def user_login(request):
  logout(request)
  username = password = ''
  if request.POST:
    email = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=email, password=password)
    if user is not None:
      if user.is_active:
        login(request, user)
        return redirect('/park')
    return render(request, 'home/login_static.html', {"login_error" : "Unrecognized username or password."})
  else:
    return render(request, 'home/login_static.html', {})

def user_logout(request):
  logout(request)
  return redirect("/")
