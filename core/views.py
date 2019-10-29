from django.shortcuts import render

from core.models import Trip, CarType


# Create your views here.


def map(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            request.user.carType = CarType.objects.get(pk=request.POST.get('carType'))
            request.user.passengers = request.POST.get('passengers')
            request.user.save()

    params = {}
    params['carTypes'] = CarType.objects.all()
    params['carUser'] = request.user.carType if request.user.is_authenticated else None
    params['passengersUser'] = request.user.passengers if request.user.is_authenticated else 1

    return render(request, 'map.html', params)


def trips(request):
    params = {}
    if request.user.is_authenticated:
        params['trips'] = Trip.objects.filter(user=request.user)
    return render(request, 'trips.html', params)


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
