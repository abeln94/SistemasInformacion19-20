from django.shortcuts import render

from core.models import Viajes, CarTypes


# Create your views here.


def mapa(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            request.user.carType = CarTypes.objects.get(pk=request.POST.get('carType'))
            request.user.save()

    params = {}
    params['carTypes'] = CarTypes.objects.all()
    params['carUser'] = request.user.carType if request.user.is_authenticated else None

    return render(request, 'mapa.html', params)

def viajes(request):
    params = {}
    if request.user.is_authenticated:
        params['viajes'] = Viajes.objects.filter(user=request.user)
    return render(request, 'viajes.html', params)

def debug(request):
    if request.method == 'POST':
        if request.POST.get('type') == 'addViaje' and request.user.is_authenticated:
            # request.user.carType = request.GET.get('type', '')
            # request.user.save()
            Viajes(
                start=request.POST.get('start'),
                end=request.POST.get('end'),
                points=request.POST.get('points'),
                user=request.user
            ).save()
            request.user.points += int(request.POST.get('points'))
            request.user.save()

        if request.POST.get('type') == 'addCarType':
            CarTypes(display=request.POST.get('carType')).save()

    # CarTypes(display="Tipo A").save()
    # CarTypes(display="Tipo B").save()
    # CarTypes(display="Tipo C").save()
    # CarTypes(display="Tipo D").save()

    return render(request, 'debug.html')
