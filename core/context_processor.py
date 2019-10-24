def context_processor(request):
    return {
        'user_label': getUserLabel(request.user),
    }


def getUserLabel(user):
    return "Hola {}, tienes {} puntos.".format(
        user.username,
        user.points, #Viajes.objects.filter(user=user).aggregate(points=Sum('points'))['points']
    ) if user.is_authenticated else ''

