from django.urls import path
from . import views


urlpatterns = [
    path('', views.rest, name='rest'),
    path('result/', views.forecast, name='forecast'), 
]