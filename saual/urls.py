from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

app_name = 'saual'
urlpatterns = [
    path('', views.saual_betin_korsetu, name='saual_beti'),
]