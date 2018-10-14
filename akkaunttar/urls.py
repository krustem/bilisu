from django.urls import path, include
from . import views

app_name = "akkaunttar"
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profiliniz/', views.profil, name='profil_ui'),
    path('tirkelu/', views.tirkelu, name='tirkelu'),
]
