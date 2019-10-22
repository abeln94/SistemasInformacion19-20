from django.http import HttpResponse

# Create your views here.
from core.models import Viajes


def debug(request):
    request.user.carType = request.GET.get('type', '')
    request.user.save()

    Viajes(start="ABC1", end="XYZ1", points=5, user=request.user).save()
    Viajes(start="ABC2", end="XYZ2", points=6, user=request.user).save()
    Viajes(start="ABC3", end="XYZ3", points=7, user=request.user).save()
    Viajes(start="ABC4", end="XYZ4", points=8, user=request.user).save()
    Viajes(start="ABC5", end="XYZ5", points=9, user=request.user).save()

    return HttpResponse("done")
