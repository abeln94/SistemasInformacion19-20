from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    path('baja', TemplateView.as_view(template_name='baja.html'), name='baja'),
    path('contacto', TemplateView.as_view(template_name='contacto.html'), name='contacto'),
    path('login', TemplateView.as_view(template_name='login.html'), name='login'),
    path('logup', TemplateView.as_view(template_name='logup.html'), name='logup'),
    path('mapa', TemplateView.as_view(template_name='mapa.html'), name='mapa'),
]
