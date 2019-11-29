import random

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import generic

from core.maps import getDistance, TooManyRequests
from core.models import Trip, CarType, User, Post


# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'


def map(request):
    params = {}
    if request.method == 'POST':
        params['source_form'] = request.POST.get('source')
        params['dest_form'] = request.POST.get('dest')

        cartype = CarType.objects.get(pk=request.POST.get('carType'))
        if request.user.is_authenticated:
            request.user.carType = cartype
            request.user.passengers = request.POST.get('passengers')
            request.user.save()

        if params['source_form'] is '' or params['dest_form'] is '':
            params['error'] = True
        else:
            try:
                dist, source, dest = getDistance(params['source_form'], params['dest_form'])
                params['costCar'] = dist * cartype.contaminationRate / int(request.POST.get('passengers'))
                params['costBus'] = dist * random.uniform(0.1, 0.9)
                params['percentDiff'] = params['costBus'] / params['costCar'] * 100
                params['source'] = source
                params['dest'] = dest
            except TooManyRequests:
                params['toomanyrequests'] = True

    params['carTypes'] = CarType.objects.all()
    params['carUser'] = request.user.carType if request.user.is_authenticated \
        else CarType.objects.get(pk=request.POST.get('carType')) if request.method == 'POST' \
        else None
    params['passengersUser'] = request.user.passengers if request.user.is_authenticated \
        else request.POST.get('passengers') if request.method == 'POST' \
        else 1

    return render(request, 'map.html', params)


def user(request):
    params = {}
    if request.user.is_authenticated:
        params['trips'] = Trip.objects.filter(user=request.user)
    return render(request, 'user.html', params)


def signup(request):
    params = {}
    if request.method == 'POST':

        params['first_name'] = first_name = request.POST.get('first_name')
        params['last_name'] = last_name = request.POST.get('last_name')
        params['email'] = email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        if '' in (first_name, last_name, email, password, repassword):
            params.setdefault('errors', {})['empty'] = True
            print('empty data')

        if password != '' and password != repassword:
            params.setdefault('errors', {})['password'] = True
            print('invalid password')

        if email != '' and User.objects.filter(email=email).exists():
            params.setdefault('errors', {})['registered'] = True
            print('invalid email')

        if not request.POST.get('remember'):
            params.setdefault('errors', {})['not_accepted'] = True
            print('invalid email')

        if 'errors' not in params:
            print('correct', params)
            User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)
            user = authenticate(email=email, password=password)
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


def deleteUser(request):
    if request.method != 'POST':
        return render(request, 'delete.html')

    if not request.user.is_authenticated:
        return redirect('home')

    if 'delete' not in request.POST:
        return redirect('user')

    request.user.delete()
    return redirect('logout')


def contact(request):
    params = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        reason = request.POST.get('reason')
        message = request.POST.get('message')
        print("Message received:")
        print(email)
        print(reason)
        print(message)
        print("It was correctly ommited")
        params['sent'] = True
    return render(request, 'contact.html', params)
