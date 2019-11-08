from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from core.maps import getDistance
from core.models import Trip, CarType, User


# Create your views here.


def map(request):
    params = {}
    if request.method == 'POST':
        if request.user.is_authenticated:
            request.user.carType = CarType.objects.get(pk=request.POST.get('carType'))
            request.user.passengers = request.POST.get('passengers')
            request.user.save()
        getDistance()

    params['carTypes'] = CarType.objects.all()
    params['carUser'] = request.user.carType if request.user.is_authenticated else None
    params['passengersUser'] = request.user.passengers if request.user.is_authenticated else 1

    return render(request, 'map.html', params)


def trips(request):
    params = {}
    if request.user.is_authenticated:
        params['trips'] = Trip.objects.filter(user=request.user)
    return render(request, 'trips.html', params)


def signup(request):
    params = {}
    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        if password != repassword:
            params.setdefault('errors',{})['password'] = True
            print('invalid password')

        if User.objects.filter(username=username).exists():
            params.setdefault('errors',{})['registered'] = True
            print('invalid username')
        if User.objects.filter(email=email).exists():
            params.setdefault('errors',{})['registered'] = True
            print('invalid email')

        if 'errors' not in params:
            print('correct', params)
            User.objects.create_user(username, email, password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

    return render(request, 'signup.html', params)


def debug(request):
    if request.method == 'POST':
        if request.POST.get('type') == 'addTrip' and request.user.is_authenticated:
            # request.user.carType = request.GET.get('type', '')
            # request.user.save()
            Trip(
                start=request.POST.get('start'),
                end=request.POST.get('end'),
                points=request.POST.get('points'),
                date=request.POST.get('date'),
                user=request.user
            ).save()
            request.user.points += int(request.POST.get('points'))
            request.user.save()

        if request.POST.get('type') == 'addCarType':
            CarType(
                model=request.POST.get('model'),
                contaminationRate=request.POST.get('contaminationRate')
            ).save()

    return render(request, 'debug.html')
