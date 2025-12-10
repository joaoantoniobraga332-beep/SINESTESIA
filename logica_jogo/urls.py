from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('jogar/', views.jogo, name='jogo'),
    path('resultado/', views.resultado, name='resultado'),
]
