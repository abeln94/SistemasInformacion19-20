"""sistInf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import TemplateView

from core import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),

    path('baja', TemplateView.as_view(template_name='baja.html'), name='baja'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('map', views.map, name='map'),
    path('user', views.user, name='user'),
    path('delete', views.deleteUser, name="delete"),

    path('api', views.api),
]


