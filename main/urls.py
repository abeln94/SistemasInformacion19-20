from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('baja', TemplateView.as_view(template_name='baja.html'), name='baja'),
    path('contacto', TemplateView.as_view(template_name='contacto.html'), name='contacto'),
    path('logup', TemplateView.as_view(template_name='logup.html'), name='logup'),
    path('mapa', TemplateView.as_view(template_name='mapa.html'), name='mapa'),

    path('accounts/', include('django.contrib.auth.urls')),
]
