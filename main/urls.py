from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    path('baja.html', TemplateView.as_view(template_name='baja.html'), name='baja'),
    path('contacto.html', TemplateView.as_view(template_name='contacto.html'), name='contacto'),
    path('index.html', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login.html', TemplateView.as_view(template_name='login.html'), name='login'),
    path('logup.html', TemplateView.as_view(template_name='logup.html'), name='logup'),
    path('mapa.html', TemplateView.as_view(template_name='mapa.html'), name='mapa'),
]
