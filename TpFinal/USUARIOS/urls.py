from django.urls import path, include
from . import views

app_name = "USUARIOS"
urlpatterns = [
    path('registrarse', views.registrarse, name="registrarse"),
]